from django.contrib.auth.models import User
from django.db import models


class ShoppingList(models.Model):
    name = models.CharField(max_length=240)
    is_archived = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
