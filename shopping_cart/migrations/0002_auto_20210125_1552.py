# Generated by Django 3.1.5 on 2021-01-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='products',
            field=models.ManyToManyField(null=True, to='products.Product'),
        ),
    ]
