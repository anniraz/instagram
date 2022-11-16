from rest_framework import viewsets,permissions,generics

from apps.stories.models import Stories,Archive
from apps.stories.serializers import StoriesSerializer,ArchiveSerializer
from apps.stories.permissions import IsOwner


class StoriesApiViewSet(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            return (IsOwner(),permissions.IsAdminUser(), )
        else:
            return (permissions.AllowAny(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class ArchiveApiView(generics.ListAPIView):
    serializer_class = ArchiveSerializer
    permission_classes=[IsOwner]

    def get_queryset(self):
        return Archive.objects.filter(user=self.request.user)

class MyArchiveApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArchiveSerializer
    permission_classes=[IsOwner]

    def get_queryset(self):
        return Archive.objects.filter(user=self.request.user)






