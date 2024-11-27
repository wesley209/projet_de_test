from django.test import TestCase
from website.models import SiteInfo, SocialCount, Newsletter

class SiteInfoModelTestCase(TestCase):
    def setUp(self):
        """Configuration initiale."""
        self.site_info = SiteInfo.objects.create(
            email="contact@exemple.com",
            nom="Mon Site",
            telephone=123456789,
            description="Description de mon site.",
            logo="logo/site/logo.png",
        )

    def test_site_info_creation(self):
        """Test de la création d'une instance SiteInfo."""
        self.assertEqual(self.site_info.email, "contact@exemple.com")
        self.assertEqual(self.site_info.nom, "Mon Site")
        self.assertEqual(self.site_info.telephone, 123456789)
        self.assertTrue(self.site_info.status)


class SocialCountModelTestCase(TestCase):
    def setUp(self):
        """Configuration initiale."""
        self.social_count = SocialCount.objects.create(
            nom="Facebook",
            lien="https://facebook.com",
            icones="fa-facebook-f",
        )

    def test_social_count_creation(self):
        """Test de la création d'une instance SocialCount."""
        self.assertEqual(self.social_count.nom, "Facebook")
        self.assertEqual(self.social_count.lien, "https://facebook.com")
        self.assertEqual(self.social_count.icones, "fa-facebook-f")
        self.assertTrue(self.social_count.status)



class NewsletterModelTestCase(TestCase):
    def setUp(self):
        """Configuration initiale."""
        self.newsletter = Newsletter.objects.create(
            email="newsletter@exemple.com",
        )

    def test_newsletter_creation(self):
        """Test de la création d'une instance Newsletter."""
        self.assertEqual(self.newsletter.email, "newsletter@exemple.com")
        self.assertTrue(self.newsletter.status)

    def test_str_representation(self):
        """Test de la méthode __str__."""
        self.assertEqual(str(self.newsletter), "newsletter@exemple.com")


# Create your tests here.
