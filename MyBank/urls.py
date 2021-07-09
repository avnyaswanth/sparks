from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Customers/',include('Customers.urls')),
    path('admin/', admin.site.urls),
]