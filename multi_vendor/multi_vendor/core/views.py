from django.shortcuts import render, redirect
from django.views import generic as views, View

from multi_vendor.core.forms import ContactForm
from multi_vendor.product.models import Product


class HomeView(views.TemplateView):
    template_name = 'core/frontpage.html'

    def get_context_data(self, **kwargs):
        context = {'newest_products': Product.objects.all()[0:8]}
        return context


class ContactView(views.View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/success_contact.html')


class AboutView(views.TemplateView):
    template_name = 'core/about.html'
