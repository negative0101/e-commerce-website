from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse



class URLtest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'pass123test'
        self.repeat_password = 'pass123test'

    def test_home_url_on_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_vendors_url_on_success(self):
        response = self.client.get('/vendors/')
        self.assertEqual(response.status_code, 200)

    def test_become_vendor_view_name(self):
        response = self.client.get(reverse('become_vendor'))
        self.assertEqual(response.status_code, 200)

    def test_become_vendor_form_(self):
        response = self.client.post(reverse('become_vendor'), data={
            'username': self.username,
            'password1': self.password,
            'password2': self.repeat_password,
        })
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(),1)
