from django.urls import include, path, re_path
from rest_framework import routers
from .views import index
from apps.auth import urls as auth_urls
from apps.lists import views as lists_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'lists', lists_views.ShoppingListViewSet, basename='ShoppingList')

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^api/auth/', include(auth_urls)),
    re_path(r'^api/', include(router.urls)),
]
