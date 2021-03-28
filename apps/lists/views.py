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

    def get_queryset(self):
        queryset = ShoppingList.objects.filter(created_by=self.request.user).all().order_by('-created_at')
        return queryset
