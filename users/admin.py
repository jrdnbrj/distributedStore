from django.contrib import admin
from users.models import User
from products.models import Product
from shopping_cart.models import ShoppingCart

admin.site.register(User)
admin.site.register(Product)
admin.site.register(ShoppingCart)
