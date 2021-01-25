from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', 'cirlces'), namespace='user')),
    # path('', include('products.urls')),
    # path('', include('shopping_cart.urls')),
    # path('', include('orders.urls')),

]
