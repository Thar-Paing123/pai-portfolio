from pathlib import Path
from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class PortfolioTests(TestCase):
    def test_home_renders_resume_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Phyo Thet Paing')
        self.assertContains(response, 'Enterprise AI Platform')
        self.assertContains(response, '365 INFOTECH')
        self.assertContains(response, 'Yoma Fleet')
        self.assertContains(response, 'The FireFocus')
        self.assertContains(response, 'Indochina Development Partner Sole Lao')
        self.assertContains(response, 'paingphyothet561@gmail.com')
        self.assertContains(response, 'data-category=', count=41)

    def test_resume_download_matches_original_asset(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('attachment;', response['Content-Disposition'])
        downloaded = b''.join(response.streaming_content)
        original = Path(settings.BASE_DIR / 'portfolio/static/portfolio/assets/resume.pdf').read_bytes()
        self.assertEqual(downloaded, original)
        self.assertTrue(downloaded.startswith(b'%PDF'))
