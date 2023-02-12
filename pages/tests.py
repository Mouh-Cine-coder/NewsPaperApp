from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_view(self):
        pass