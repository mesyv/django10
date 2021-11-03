from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.

#It's added from the book "Django for Beginners 3.1"
class SimpleTests(SimpleTestCase):  
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/calculator/')
        self.assertEqual(response.status_code, 200)