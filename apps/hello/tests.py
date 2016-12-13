from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class ViewsTests(TestCase):
    def test_index(self):
        """
        Check index page
        """
        client = Client()
        response = client.get(reverse('index'))
        self.assertContains(response, "Clara")
        self.assertContains(response, "Contacts")
