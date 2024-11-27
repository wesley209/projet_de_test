from django.test import TestCase
from django.utils.text import slugify
from elenizado.models import (
    Categorie, Publication, Commentaire, ReponseCommentaire, Evenement, Cours, Textes, Video
)
from django.core.files.uploadedfile import SimpleUploadedFile

class ModelsIntegrationTestCase(TestCase):

    def setUp(self):
        """Création des objets pour les tests d'intégration."""
        # Fichiers temporaires
        self.image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.file_pdf = SimpleUploadedFile("test_file.pdf", b"file_content", content_type="application/pdf")

        # Création de la catégorie
        self.categorie = Categorie.objects.create(
            nom="Test Categorie",
            description="Description de la catégorie"
        )

        # Création de la publication
        self.publication = Publication.objects.create(
            titre="Test Publication",
            description="<p>Test HTML</p>",
            image=self.image_file,
            categorie=self.categorie
        )

        # Création du commentaire
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Jean Dupont",
            email="jean.dupont@example.com",
            commentaire="Ceci est un commentaire."
        )

        # Création de la réponse au commentaire
        self.reponse = ReponseCommentaire.objects.create(
            commentaire=self.commentaire,
            nom="Alice",
            email="alice@example.com",
            reponse="Merci pour le commentaire."
        )

    def test_publication_with_commentaire_and_reponse(self):
        """Test d'intégration : Publication avec commentaire et réponse."""
        # Vérifier la publication
        self.assertEqual(self.publication.titre, "Test Publication")
        self.assertEqual(self.publication.categorie, self.categorie)
        self.assertTrue(self.publication.slug.startswith(slugify("Test Publication")))

        # Vérifier le commentaire
        self.assertEqual(self.commentaire.publication, self.publication)
        self.assertEqual(self.commentaire.nom, "Jean Dupont")
        self.assertEqual(self.commentaire.commentaire, "Ceci est un commentaire.")

        # Vérifier la réponse au commentaire
        self.assertEqual(self.reponse.commentaire, self.commentaire)
        self.assertEqual(self.reponse.nom, "Alice")
        self.assertEqual(self.reponse.reponse, "Merci pour le commentaire.")

    def test_interactions_with_events_and_courses(self):
        """Test d'intégration : Interaction avec événements et cours."""
        evenement = Evenement.objects.create(
            titre="Test Evenement",
            description="Description de l'événement.",
            image=self.image_file
        )
        self.assertEqual(evenement.titre, "Test Evenement")
        self.assertTrue(evenement.slug.startswith(slugify("Test Evenement")))

        cours = Cours.objects.create(
            titre="Cours Python",
            niveau="Débutant",
            annee=2024,
            description="Cours sur Python.",
            image=self.image_file,
            cours=self.file_pdf
        )
        self.assertEqual(cours.titre, "Cours Python")
        self.assertEqual(cours.niveau, "Débutant")

    def test_texts_and_videos(self):
        """Test d'intégration : Textes et vidéos."""
        texte = Textes.objects.create(
            titre="Documentation Django",
            description="Guide complet sur Django.",
            image=self.image_file,
            pdf=self.file_pdf
        )
        self.assertEqual(texte.titre, "Documentation Django")

        video = Video.objects.create(
            titre="Vidéo Test",
            description="Description de la vidéo.",
            image=self.image_file,
            video="https://www.youtube.com/watch?v=12345ABC"
        )
        self.assertEqual(video.get_video, "12345ABC")
