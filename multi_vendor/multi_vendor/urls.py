from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('vendors/', include('multi_vendor.vendor.urls')),
                  path('cart/', include('multi_vendor.cart.urls')),
                  path('', include('multi_vendor.core.urls')),
                  path('', include('multi_vendor.product.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
