from django.shortcuts import render, redirect
import stripe
from django.views import generic as views

from multi_vendor.cart.cart import Cart
from django.conf import settings
from django.contrib import messages
from .forms import CheckoutForm

from multi_vendor.order.utils import checkout


class CartDetailsView(views.View):
    def post(self, request):
        cart = Cart(request)
        form = CheckoutForm(request.POST)

        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe_token = form.cleaned_data['stripe_token']
            try:
                charge = stripe.Charge.create(
                    amount=int(cart.get_total_cost() * 100),
                    currency='USD',
                    description='Charge from shop',
                    source=stripe_token
                )

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                place = form.cleaned_data['place']

                order = checkout(request, first_name, last_name, email, address, zipcode, place, phone,
                                 cart.get_total_cost())
                cart.clear()
                return redirect('success')
            except Exception:
                messages.error(request, 'There was something wrong with the payment')

    def get(self, request):
        cart = Cart(request)
        form = CheckoutForm()

        remove_from_cart = request.GET.get('remove_from_cart', '')
        change_quantity = request.GET.get('change_quantity', '')
        quantity = request.GET.get('quantity', 0)

        if remove_from_cart:
            cart.remove(remove_from_cart)
            return redirect('cart')

        if change_quantity:
            cart.add(change_quantity, quantity, True)

            return redirect('cart')

        return render(request, 'cart/cart.html', {'form': form, 'stripe_pub_key': settings.STRIPE_PUB_KEY})


class SuccessView(views.TemplateView):
    template_name = 'cart/success.html'
