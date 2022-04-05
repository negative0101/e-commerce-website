from django.test import TestCase
from django.urls import reverse

from multi_vendor.product.forms import AddToCartForm
from multi_vendor.product.models import Product, Category


class ProductViewTest(TestCase):

    def test_valid_AddToCartForm(self):
        data = {'quantity': 1}
        form = AddToCartForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_AddToCartForm(self):
        data = {'quantity': 'assd'}
        form = AddToCartForm(data=data)
        self.assertFalse(form.is_valid())


class CategoryViewTest(TestCase):

    def test_GET_view_url_exists_at_desired_location(self):
        test = Category.objects.create(
            title='default',
            slug='default'
        )
        response = self.client.get(reverse('category', args=([test.slug])))
        self.assertEqual(response.status_code, 200)

    def test_GET_view_url_404_on_wrong_input(self):
        test = Category.objects.create(
            title='default',
            slug='default'
        )
        response = self.client.get(reverse('category', args=([test.slug + '1'])))
        self.assertEqual(response.status_code, 404)
