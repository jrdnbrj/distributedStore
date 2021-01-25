from django.db import models
from django.contrib.auth.models import AbstractUser
from shopping_cart.models import ShoppingCart
from products.models import Product

class User(AbstractUser):
    shopping_cart = models.OneToOneField(
        ShoppingCart,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    products = models.ManyToManyField(Product, null=True, blank=True)
    # REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.username