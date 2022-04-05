from django.urls import path

from multi_vendor.cart import views

urlpatterns = [
    path('', views.CartDetailsView.as_view(), name='cart'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
