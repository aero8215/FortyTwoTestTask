from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import PersonalData

class ViewsTests(TestCase):
    def test_index(self):
        """
        Check index page
        """
        client = Client()
        response = client.get(reverse('index'))
        self.assertContains(response, "Clara")
        self.assertContains(response, "Contacts")


class PersonalDataTest(TestCase):
     def setUp(self):
         PersonalData.objects.create(first_name="Charles", last_name="Chaplin",bio="bla bla bla", birth_date="1990-12-20")

     def test_personal_data(self):
         obj = PersonalData.objects.get(first_name="Charles")
         self.assertEqual(obj.first_name, "Charles")
         self.assertEqual(obj.last_name, "Chaplin")
