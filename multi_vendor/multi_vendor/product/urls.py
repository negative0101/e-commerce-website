from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
    path('<slug:category_slug>/', views.CategoryView.as_view(), name='category'),

    path('vendors/vendor-admin/add-product/', views.CreateProductView.as_view(), name='add_product'),
    path('vendor-admin/edit-product/<int:pk>/', views.EditProductView.as_view(), name='edit product'),
    path('vendor-admin/delete-product/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),
]
