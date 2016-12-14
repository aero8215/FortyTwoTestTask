from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import Information

class ViewsTests(TestCase):
    def test_index(self):
        """
        Check index page
        """
        client = Client()
        response = client.get(reverse('index'))
        self.assertContains(response, "Clara")
        self.assertContains(response, "Contacts")


class InformationTest(TestCase):
     def setUp(self):
         Information.objects.create(first_name="Charles", last_name="Chaplin", bio="bla bla bla", birth_date="1990-12-20")

     def test_information_data(self):
         obj = Information.objects.get(first_name="Charles")
         self.assertEqual(obj.first_name, "Charles")
         self.assertEqual(obj.last_name, "Chaplin")
