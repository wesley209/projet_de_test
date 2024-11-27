from django.test import TestCase
from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie
from django.core.files.uploadedfile import SimpleUploadedFile

class ModelsIntegrationTestCase(TestCase):

    def setUp(self):
        """Configuration des objets pour les tests d'intégration."""
        # Fichiers temporaires
        self.image_file = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg"
        )
        self.file_cv = SimpleUploadedFile(
            "test_cv.pdf", b"file_content", content_type="application/pdf"
        )

        # Création de base pour les tests
        self.curriculum = Curriculum.objects.create(
            photo=self.image_file,
            nom="Test Nom",
            description="<p>Test description</p>",
            cv=self.file_cv
        )

        self.contact = Contact.objects.create(
            nom="Jean Dupont",
            email="jean.dupont@example.com",
            subject="Demande d'information",
            telephone=123456789,
            message="Bonjour, je voudrais en savoir plus sur vos services."
        )

        self.prestation = Prestation.objects.create(
            titre="Test Prestation",
            description="Description de la prestation",
            image=self.image_file
        )

        self.presentation = Presentation.objects.create(
            titre="Présentation Test",
            description="<p>Description HTML</p>",
            image=self.image_file
        )

        self.gallerie = Gallerie.objects.create(
            gallerie=self.image_file,
            titre="Image de la gallerie"
        )

    def test_curriculum_and_contact_integration(self):
        """Test d'intégration entre Curriculum et Contact."""
        # Vérifier que les deux objets peuvent coexister sans conflit
        self.assertEqual(self.curriculum.nom, "Test Nom")
        self.assertEqual(self.contact.nom, "Jean Dupont")
        self.assertEqual(self.contact.email, "jean.dupont@example.com")
        self.assertIn("Test description", self.curriculum.description)

    def test_prestation_and_presentation_integration(self):
        """Test d'intégration entre Prestation et Presentation."""
        # Vérifier que les titres et descriptions sont correctement configurés
        self.assertEqual(self.prestation.titre, "Test Prestation")
        self.assertEqual(self.presentation.titre, "Présentation Test")
        self.assertIn("Description de la prestation", self.prestation.description)
        self.assertIn("HTML", self.presentation.description)

    def test_gallerie_and_curriculum_integration(self):
        """Test d'intégration entre Gallerie et Curriculum."""
        # Vérifier que les objets partagent des ressources sans conflit
        self.assertEqual(self.gallerie.titre, "Image de la gallerie")
        self.assertTrue(self.gallerie.status)
        self.assertEqual(self.curriculum.nom, "Test Nom")

    def test_all_models_coexistence(self):
        """Test de coexistence de tous les modèles."""
        # Vérifier que tous les objets existent simultanément sans conflit
        self.assertEqual(Curriculum.objects.count(), 1)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Prestation.objects.count(), 1)
        self.assertEqual(Presentation.objects.count(), 1)
        self.assertEqual(Gallerie.objects.count(), 1)
