from django.test import TestCase
from website.models import SiteInfo, SocialCount, Newsletter

class IntegrationTestCase(TestCase):
    def setUp(self):
        """Configuration initiale pour les tests d'intégration."""
        # Créer une instance de SiteInfo
        self.site_info = SiteInfo.objects.create(
            email="contact@exemple.com",
            nom="Mon Site",
            telephone=123456789,
            description="Description de mon site.",
            logo="logo/site/logo.png",
        )

        # Ajouter des réseaux sociaux au site
        self.social_facebook = SocialCount.objects.create(
            nom="Facebook",
            lien="https://facebook.com",
            icones="fa-facebook-f",
        )
        self.social_twitter = SocialCount.objects.create(
            nom="Twitter",
            lien="https://twitter.com",
            icones="fa-twitter",
        )

        # Créer une entrée dans la newsletter
        self.newsletter = Newsletter.objects.create(
            email="newsletter@exemple.com",
        )

    def test_site_info_with_social_count(self):
        """Vérifier que les réseaux sociaux sont correctement associés au site."""
        # Vérification de l'instance SiteInfo
        self.assertEqual(self.site_info.nom, "Mon Site")
        self.assertEqual(self.site_info.email, "contact@exemple.com")

        # Vérification des réseaux sociaux
        social_links = SocialCount.objects.all()
        self.assertEqual(social_links.count(), 2)
        self.assertIn(self.social_facebook, social_links)
        self.assertIn(self.social_twitter, social_links)

    def test_newsletter_subscription(self):
        """Vérifier que l'abonnement à la newsletter fonctionne."""
        # Vérification de l'email de la newsletter
        self.assertEqual(self.newsletter.email, "newsletter@exemple.com")
        self.assertTrue(self.newsletter.status)

    def test_full_integration(self):
        """Vérifier l'intégration complète entre SiteInfo, SocialCount et Newsletter."""
        # Vérification des données du site
        self.assertEqual(SiteInfo.objects.count(), 1)
        self.assertEqual(self.site_info.nom, "Mon Site")

        # Vérification des réseaux sociaux
        social_links = SocialCount.objects.all()
        self.assertEqual(social_links.count(), 2)
        self.assertEqual(social_links[0].nom, "Facebook")
        self.assertEqual(social_links[1].nom, "Twitter")

        # Vérification de la newsletter
        self.assertEqual(Newsletter.objects.count(), 1)
        self.assertEqual(Newsletter.objects.first().email, "newsletter@exemple.com")
