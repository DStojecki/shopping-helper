from .models import ShoppingList
from rest_framework import viewsets
from .serializers import ShoppingListSerializer
from apps.auth.permissions import OwnerOnly


class ShoppingListViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing, creating and updating lists
    """
    permission_classes = [OwnerOnly]
    serializer_class = ShoppingListSerializer
    queryset = ShoppingList.objects.all().order_by('-created_at')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)
