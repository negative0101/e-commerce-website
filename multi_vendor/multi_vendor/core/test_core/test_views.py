from django.test import TestCase, Client
from django.urls import reverse


class TestHomeView(TestCase):

    def setUp(self):
        self.test_client = Client()

    def test_correct_template(self):
        response = self.test_client.get(reverse('frontpage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/frontpage.html')

    def test_context_data(self):
        response = self.test_client.get(reverse('frontpage'))
        print(response)
        self.assertEqual(
            len(response.context_data['newest_products']), 0
        )


class TestContactView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_correct_template(self):
        response = self.test_client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')

    def test_context_data(self):
        response = self.test_client.get(reverse('contact'))
        self.assertEqual(
            (response.context_data['total_products_num']), 0
        )


class TestAboutView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_correct_template(self):
        response = self.test_client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
