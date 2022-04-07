from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views import generic as views
from .models import Vendor


class VendorAdminView(auth_mixin.LoginRequiredMixin, views.View):
    def get(self, request):
        vendor = request.user.vendor
        products = vendor.products.all()
        orders = vendor.orders.all()

        return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'product': products, 'orders': orders})


class AllVendorsView(views.TemplateView):
    template_name = 'vendor/vendors.html'

    def get_context_data(self, **kwargs):
        context = {'vendors': Vendor.objects.all()}
        return context


class VendorView(views.View):
    def get(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        return render(request, 'vendor/vendor.html', {'vendor': vendor})


class CreateVendorView(views.View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'vendor/become_vendor.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user) #create user in db to vendor
            return redirect('frontpage')

        return render(request, 'vendor/become_vendor.html', {'form': form})





