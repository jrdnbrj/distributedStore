from django.db import models
from products.models import Product

class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)