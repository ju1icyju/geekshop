from django.urls import path
from mainapp.views import products, contact

urlpatterns = [
    path('products/<int:pk>', products, name='product'),
    path('contact/', contact, name="contact"),
]