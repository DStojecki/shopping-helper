from django.contrib.auth.models import User
from django.db import models
from ..lists.models import ShoppingList


class Category(models.Model):
    name = models.CharField(max_length=240)
    color = models.CharField(max_length=6)
    list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, null=True, related_name='categories')

    def __str__(self):
        return self.name
