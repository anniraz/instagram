from rest_framework import viewsets
from rest_framework import permissions

from apps.favorites.models import Favorite,FavoriteCategory
from apps.favorites.serializers import FavoriteSerializer,FavoriteCategorySerializer
from apps.user.permissions import IsOwner

class FavoriteCategoryApiViewSet(viewsets.ModelViewSet):
    # your own category(favorite) 

    queryset=FavoriteCategory.objects.all()
    serializer_class=FavoriteCategorySerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            return (IsOwner(),permissions.IsAdminUser(), )
        else:
            return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class FavoriteApiViewSet(viewsets.ModelViewSet):
    # your own favorites

    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            return (IsOwner(),permissions.IsAdminUser(), )
        else:
            return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)







