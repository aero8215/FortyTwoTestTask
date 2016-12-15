from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import Information


def setup_data():
    first_name = "Charles"
    last_name = "Chaplin"
    bio = "bla bla bla"
    birth_date = "1990-12-20T00:00:00Z"
    Information.objects.create(first_name=first_name,
                               last_name=last_name,
                               bio=bio,
                               birth_date=birth_date)


class ViewsTests(TestCase):
    def setUp(self):
        setup_data()

    def test_index(self):
        '''
        Test index view
        '''
        client = Client()
        response = client.get(reverse('index'))
        self.assertContains(response, "Charles")
        self.assertContains(response, "Contacts")


class InformationTest(TestCase):
    def setUp(self):
        setup_data()

    def test_information_data(self):
        '''
        Test Information model
        '''
        obj = Information.objects.get(first_name="Charles")
        self.assertEqual(obj.first_name, "Charles")
        self.assertEqual(obj.last_name, "Chaplin")
        self.assertEqual(obj.bio, "bla bla bla")
