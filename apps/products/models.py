from django.contrib.auth.models import User
from django.db import models
from ..categories.models import Category


class Product(models.Model):
    product = models.CharField(max_length=240)
    quantity = models.IntegerField(null=False)
    type = models.CharField(
        max_length=3,
        choices=[
            ('szt', 'sztuk'),
            ('g', 'gram'),
            ('kg', 'kilogramów'),
            ('ml', 'mililitrów'),
            ('l', 'litrów')
        ],
        default='szt'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')

    def __str__(self):
        return self.name
