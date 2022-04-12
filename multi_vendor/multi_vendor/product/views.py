from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
import random
from django import views
from django.utils.text import slugify


from .forms import AddToCartForm, ProductForm, DeleteProductForm
from .models import Category, Product
from ..cart.cart import Cart
from django.contrib.auth import mixins as auth_mixin

MESSAGE_FOR_ADDING_PRODUCT_SUCCESS = "Product was added to basket!"
NUMBER_OF_RANDOM_SIMILAR_ITEMS = 4


class ProductView(views.View):
    def get(self, request, category_slug, product_slug):
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        form = AddToCartForm()
        similar_products = list(product.category.products.exclude(id=product.id))

        if len(similar_products) >= NUMBER_OF_RANDOM_SIMILAR_ITEMS:
            similar_products = random.sample(similar_products, NUMBER_OF_RANDOM_SIMILAR_ITEMS)

        return render(request, 'product/product.html',
                      {'product': product, 'similar_products': similar_products, 'form': form})

    def post(self, request, category_slug, product_slug):
        cart = Cart(request)
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity)
            messages.success(request, MESSAGE_FOR_ADDING_PRODUCT_SUCCESS)
            return redirect('product', category_slug=category_slug, product_slug=product_slug)
        return render(request, 'product/product.html',
                      {'product': product, 'form': form})


class CreateProductView(auth_mixin.LoginRequiredMixin, views.View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product/add_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()
            return redirect('vendor_admin')
        return render(request, 'product/add_product.html', {'form': form})


class EditProductView(auth_mixin.LoginRequiredMixin, views.View):
    def get(self, request, pk):
        vendor = request.user.vendor
        product = vendor.products.get(pk=pk)

        form = ProductForm(instance=product)
        return render(request, 'product/edit_product.html', {'form': form, 'product': product, })

    def post(self, request, pk):
        vendor = request.user.vendor
        product = vendor.products.get(pk=pk)

        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('frontpage')
        return render(request, 'product/edit_product.html', {'form': form, 'product': product})


class DeleteProductView(auth_mixin.LoginRequiredMixin, views.View):
    def get(self, request, pk):
        vendor = request.user.vendor
        product = vendor.products.get(pk=pk)

        form = DeleteProductForm(instance=product)
        return render(request, 'product/delete.html', {'form': form, 'product': product, })

    def post(self, request, pk):
        vendor = request.user.vendor
        product = vendor.products.get(pk=pk)

        form = DeleteProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('vendor_admin')
        return render(request, 'product/delete.html', {'form': form, 'product': product})


class CategoryView(views.View):
    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)

        return render(request, 'product/category.html', {'category': category})


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})
