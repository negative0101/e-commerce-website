from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from multi_vendor.vendor.models import Vendor


class TestVendorModel(TestCase):
    def test_model_str(self):
        testuser = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(str(testuser.username), 'testuser')
    #
    # def test_model_db(self):
    #     testuser = User(username='testuser', password='12345')
    #     testuser.full_clean()
    #     testuser.save()
    #     self.assertIsNotNone(testuser)
