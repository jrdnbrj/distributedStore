from django.db import models
from django.contrib.auth.models import AbstractUser
from shopping_cart.models import ShoppingCart
from products.models import Product

class User(AbstractUser):
    shopping_cart = models.OneToOneField(
        ShoppingCart,
        on_delete=models.CASCADE
    )
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
