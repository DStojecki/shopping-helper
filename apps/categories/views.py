from .models import Category
from rest_framework import viewsets
from .serializers import CategorySerializer
from apps.auth.permissions import OwnerOnly


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing, creating and updating lists
    """
    permission_classes = [OwnerOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-created_at')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)
