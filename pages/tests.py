from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):
    """Tests the home page view."""
    def test_url_location(self):
        """Tests if the URL exists in the correct location."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_avability(self):
        """Tests if the URL is available by name."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name(self):
        """Tests if the template used to load this page is correct."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        """Tests if the template has the correct headers to load the page."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Hello!</h1>')

class ProjectsPageTest(SimpleTestCase):
    """Tests the projects page view."""
    def test_url_location(self):
        """Tests if the URL exists in the correct location."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_avability(self):
        """Tests if the URL is available by name."""
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name(self):
        """Tests if the template used to load this page is correct."""
        response = self.client.get(reverse('projects'))
        self.assertTemplateUsed(response, 'projects.html')

    def test_template_content(self):
        """Tests if the template has the correct headers to load the page."""
        response = self.client.get(reverse('projects'))
        self.assertContains(response, '<h1>My Projects</h1>')

class ContactsPageTest(SimpleTestCase):
    """Tests the contacts page view."""
    def test_url_location(self):
        """Tests if the URL exists in the correct location."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_avability(self):
        """Tests if the URL is available by name."""
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name(self):
        """Tests if the template used to load this page is correct."""
        response = self.client.get(reverse('contacts'))
        self.assertTemplateUsed(response, 'contacts.html')

    def test_template_content(self):
        """Tests if the template has the correct headers to load the page."""
        response = self.client.get(reverse('contacts'))
        self.assertContains(response, '<h1>Contact Me!</h1>')