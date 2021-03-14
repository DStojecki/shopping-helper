from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from apps.auth.permissions import OwnerOnly


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing, creating and updating products
    """
    permission_classes = [OwnerOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-created_at')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)
