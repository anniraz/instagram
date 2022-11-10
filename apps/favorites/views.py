from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.favorites.models import Favorite
from apps.favorites.serializers import FavoriteSerializer

class FavoriteApiViewSet(viewsets.ModelViewSet):
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


