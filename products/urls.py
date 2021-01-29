from django.urls import path
from products.views import create_product, edit_product, delete_product

urlpatterns = [
    path('producto/crear/', create_product, name='create_product'),
    path('producto/editar/<int:id>', edit_product, name='edit_product'),
    path('producto/eliminar/<int:id>', delete_product, name='delete_product'),
]
