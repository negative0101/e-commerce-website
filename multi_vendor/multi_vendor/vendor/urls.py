from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.AllVendorsView.as_view(), name='vendors'),
    path('<int:vendor_id>/', views.VendorView.as_view(), name='vendor'),
    path('become-vendor/', views.CreateVendorView.as_view(), name='become_vendor'),
    path('vendor-admin/', views.VendorAdminView.as_view(), name='vendor_admin'),


    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),


]
