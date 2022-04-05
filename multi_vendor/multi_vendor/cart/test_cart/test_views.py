from django.test import TestCase, Client
from django.urls import reverse

from multi_vendor.cart.forms import CheckoutForm


class TestCartDetailsView(TestCase):
    def setUP(self):
        self.test_user = Client()

    def test_form_CheckotuForm(self):
        form_data = {
            'first_name': 'firstname',
            'last_name': 'lastname',
            'email': 'email@email.bg',
            'phone': '123412412',
            'address': '123dvasd adas',
            'zipcode': '1234',
            'place': 'svadavsd asd',
            'stripe_token': '1glaskvd129'}
        form = CheckoutForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestSuccessView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_correct_template(self):
        response = self.test_client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/success.html')

#
