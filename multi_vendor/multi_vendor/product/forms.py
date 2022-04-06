
from django import forms

from multi_vendor.product.models import Product


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']


class DeleteProductForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Product
        fields = ()


