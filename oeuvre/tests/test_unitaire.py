from django.test import TestCase
from oeuvre.models import Poesie

class PoesieModelTestCase(TestCase):

    def setUp(self):
        """Configuration des données pour les tests."""
        self.poesie = Poesie.objects.create(
            titre="La Beauté du Ciel",
            description="Une poésie décrivant la splendeur du ciel étoilé.",
            poeme="<p>Ô ciel étoilé, ta beauté illumine la nuit.</p>"
        )

    def test_poesie_creation(self):
        """Test de la création d'une poésie."""
        self.assertEqual(self.poesie.titre, "La Beauté du Ciel")
        self.assertEqual(self.poesie.description, "Une poésie décrivant la splendeur du ciel étoilé.")
        self.assertIn("Ô ciel étoilé", self.poesie.poeme)
        self.assertTrue(self.poesie.status)

    def test_verbose_name(self):
        """Test des métadonnées du modèle."""
        self.assertEqual(Poesie._meta.verbose_name, 'Poésie')
        self.assertEqual(Poesie._meta.verbose_name_plural, 'Poésies')

    def test_str_representation(self):
        """Test de la méthode __str__."""
        self.assertEqual(str(self.poesie), "La Beauté du Ciel")


# Create your tests here.
