from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('cart/',include('cart.urls')),
    path('accounts/', include('allauth.urls')),
    path("djangorave/", include("djangorave.urls", namespace="djangorave")),

]
