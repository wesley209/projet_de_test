from django.test import TestCase
from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile

class ModelsTestCase(TestCase):

    def setUp(self):
        # Fichiers temporaires pour les tests
        self.image_file = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg"
        )
        self.file_cv = SimpleUploadedFile(
            "test_cv.pdf", b"file_content", content_type="application/pdf"
        )

    def test_curriculum_creation(self):
        """Test de la création d'un objet Curriculum"""
        curriculum = Curriculum.objects.create(
            photo=self.image_file,
            nom="Test Nom",
            description="<p>Test description</p>",
            cv=self.file_cv
        )
        self.assertEqual(curriculum.nom, "Test Nom")
        self.assertTrue(curriculum.status)
        self.assertIn("Test description", curriculum.description)

    def test_contact_creation(self):
        """Test de la création d'un objet Contact"""
        contact = Contact.objects.create(
            nom="Jean Dupont",
            email="jean.dupont@example.com",
            subject="Demande d'information",
            telephone=123456789,
            message="Bonjour, je voudrais en savoir plus sur vos services."
        )
        self.assertEqual(contact.nom, "Jean Dupont")
        self.assertEqual(contact.email, "jean.dupont@example.com")
        self.assertEqual(contact.telephone, 123456789)

    def test_prestation_creation(self):
        """Test de la création d'un objet Prestation"""
        prestation = Prestation.objects.create(
            titre="Test Prestation",
            description="Description de la prestation",
            image=self.image_file
        )
        self.assertEqual(prestation.titre, "Test Prestation")
        self.assertTrue(prestation.status)

    def test_presentation_creation(self):
        """Test de la création d'un objet Presentation"""
        presentation = Presentation.objects.create(
            titre="Présentation Test",
            description="<p>Description HTML</p>",
            image=self.image_file
        )
        self.assertEqual(presentation.titre, "Présentation Test")
        self.assertIn("HTML", presentation.description)

    def test_gallerie_creation(self):
        """Test de la création d'un objet Gallerie"""
        gallerie = Gallerie.objects.create(
            gallerie=self.image_file,
            titre="Image de la gallerie"
        )
        self.assertEqual(gallerie.titre, "Image de la gallerie")
        self.assertTrue(gallerie.status)


# Create your tests here.
