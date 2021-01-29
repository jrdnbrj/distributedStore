from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places = 2, max_digits = 7)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name