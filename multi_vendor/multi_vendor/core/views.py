from django.shortcuts import render, redirect
from django.views import generic as views

from multi_vendor.product.models import Product


class HomeView(views.TemplateView):
    template_name = 'core/frontpage.html'

    def get_context_data(self, **kwargs):
        context = {'newest_products': Product.objects.all()[0:8]}
        return context


class ContactView(views.TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = {'total_products_num': len(Product.objects.all())}
        return context


class AboutView(views.TemplateView):
    template_name = 'core/about.html'
