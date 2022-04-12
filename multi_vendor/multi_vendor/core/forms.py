from django.forms import ModelForm

from multi_vendor.core.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

