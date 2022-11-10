from rest_framework import viewsets,permissions

from apps.stories.models import Stories
from apps.stories.serializers import StoriesSerializer
from apps.stories.permissions import IsOwner


class StoriesApiViewSet(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            return (IsOwner(), )
        else:
            return (permissions.AllowAny(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
