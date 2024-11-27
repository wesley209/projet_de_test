from django.test import TestCase
from django.utils.text import slugify
from elenizado.models import (
    Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
)
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime

class ModelsTestCase(TestCase):

    def setUp(self):
        # Fichiers temporaires pour les tests
        self.image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.file_pdf = SimpleUploadedFile("test_file.pdf", b"file_content", content_type="application/pdf")

        # Création des instances de base pour les relations
        self.categorie = Categorie.objects.create(
            nom="Test Categorie",
            description="Description de la catégorie"
        )

    def test_categorie_creation(self):
        """Test de la création d'une catégorie"""
        self.assertEqual(self.categorie.nom, "Test Categorie")
        self.assertTrue(self.categorie.status)

    def test_publication_creation(self):
        """Test de la création d'une publication avec un slug auto-généré"""
        publication = Publication.objects.create(
            titre="Test Publication",
            description="<p>Test HTML</p>",
            image=self.image_file,
            categorie=self.categorie
        )
        self.assertEqual(publication.titre, "Test Publication")
        self.assertIn("Test HTML", publication.description)
        self.assertTrue(publication.slug.startswith(slugify("Test Publication")))

    def test_commentaire_creation(self):
        """Test de la création d'un commentaire pour une publication"""
        publication = Publication.objects.create(
            titre="Test Publication",
            description="<p>Test HTML</p>",
            image=self.image_file,
            categorie=self.categorie
        )
        commentaire = Commentaire.objects.create(
            publication=publication,
            nom="Jean Dupont",
            email="jean.dupont@example.com",
            commentaire="Ceci est un commentaire."
        )
        self.assertEqual(commentaire.nom, "Jean Dupont")
        self.assertEqual(commentaire.publication, publication)

    def test_reponse_commentaire_creation(self):
        """Test de la création d'une réponse à un commentaire"""
        publication = Publication.objects.create(
            titre="Test Publication",
            description="<p>Test HTML</p>",
            image=self.image_file,
            categorie=self.categorie
        )
        commentaire = Commentaire.objects.create(
            publication=publication,
            nom="Jean Dupont",
            commentaire="Ceci est un commentaire."
        )
        reponse = ReponseCommentaire.objects.create(
            commentaire=commentaire,
            nom="Alice",
            email="alice@example.com",
            reponse="Merci pour le commentaire."
        )
        self.assertEqual(reponse.commentaire, commentaire)
        self.assertEqual(reponse.nom, "Alice")

    def test_evenement_creation(self):
        """Test de la création d'un événement avec un slug auto-généré"""
        evenement = Evenement.objects.create(
            titre="Test Evenement",
            description="<p>Description de l'événement</p>",
            image=self.image_file
        )
        self.assertEqual(evenement.titre, "Test Evenement")
        self.assertTrue(evenement.slug.startswith(slugify("Test Evenement")))

    def test_cours_creation(self):
        """Test de la création d'un cours"""
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

    def test_textes_creation(self):
        """Test de la création d'un texte de référence"""
        texte = Textes.objects.create(
            titre="Documentation Django",
            description="Guide complet sur Django.",
            image=self.image_file,
            pdf=self.file_pdf
        )
        self.assertEqual(texte.titre, "Documentation Django")

    def test_video_creation(self):
        """Test de la création d'une vidéo avec extraction d'ID"""
        video = Video.objects.create(
            titre="Vidéo Test",
            description="Description de la vidéo",
            image=self.image_file,
            video="https://www.youtube.com/watch?v=12345ABC"
        )
        self.assertEqual(video.get_video, "12345ABC")


# Create your tests here.
