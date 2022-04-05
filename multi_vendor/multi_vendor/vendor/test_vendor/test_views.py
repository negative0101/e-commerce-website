from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from multi_vendor.vendor.models import Vendor

UserModel = get_user_model()


class TestVendorsView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_ALL_vendors_GET(self):
        response = self.test_client.get(reverse('vendors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vendor/vendors.html')

    def test_login(self):
        user_data = {
            'username': 'ivo',
            'password': 'ivo123'
        }
        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code,200)


