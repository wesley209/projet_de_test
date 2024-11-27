from django.test import TestCase
from oeuvre.models import Poesie

class PoesieIntegrationTestCase(TestCase):

    def setUp(self):
        """Création des données pour les tests d'intégration."""
        self.poesie_1 = Poesie.objects.create(
            titre="La Beauté du Ciel",
            description="Une poésie décrivant la splendeur du ciel étoilé.",
            poeme="<p>Ô ciel étoilé, ta beauté illumine la nuit.</p>",
        )
        self.poesie_2 = Poesie.objects.create(
            titre="L'ombre des Nuages",
            description="Les nuages dansent dans le ciel gris.",
            poeme="<p>Dans l'ombre des nuages, je trouve la paix.</p>",
        )

    def test_multiple_poesies_creation(self):
        """Test de la création de plusieurs poésies."""
        poesies = Poesie.objects.all()
        self.assertEqual(poesies.count(), 2)
        self.assertEqual(poesies[0].titre, "La Beauté du Ciel")
        self.assertEqual(poesies[1].titre, "L'ombre des Nuages")

    def test_search_by_title(self):
        """Test de recherche d'une poésie par titre."""
        poesie = Poesie.objects.filter(titre__icontains="Beauté").first()
        self.assertIsNotNone(poesie)
        self.assertEqual(poesie.titre, "La Beauté du Ciel")

    def test_html_content_handling(self):
        """Test de gestion du contenu HTML dans l'attribut poeme."""
        poesie = Poesie.objects.get(titre="La Beauté du Ciel")
        self.assertIn("<p>", poesie.poeme)
        self.assertIn("Ô ciel étoilé", poesie.poeme)
        self.assertIn("</p>", poesie.poeme)

    def test_full_integration(self):
        """Test d'intégration complet pour les poésies."""
        # Vérification des métadonnées
        self.assertEqual(Poesie._meta.verbose_name, "Poésie")
        self.assertEqual(Poesie._meta.verbose_name_plural, "Poésies")

        # Vérification des données existantes
        poesies = Poesie.objects.all()
        self.assertEqual(poesies.count(), 2)

        # Vérification des représentations textuelles
        self.assertEqual(str(self.poesie_1), "La Beauté du Ciel")
        self.assertEqual(str(self.poesie_2), "L'ombre des Nuages")
