from django.contrib import admin

# Register your models here.
from multi_vendor.order.models import OrderItem,Order


admin.site.register(Order)
admin.site.register(OrderItem)
