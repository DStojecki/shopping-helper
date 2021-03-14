from django.contrib.auth.models import User
from django.db import models
from apps.lists.models import ShoppingList


class Category(models.Model):
    name = models.CharField(max_length=240)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    shopping_list = models.ForeignKey(
        ShoppingList,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
