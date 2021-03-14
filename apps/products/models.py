from django.contrib.auth.models import User
from django.db import models
from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=240)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    quantity_type = models.CharField(
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
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
