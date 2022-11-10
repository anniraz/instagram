from rest_framework import viewsets,permissions

from apps.post.serializers import PostSerializer,PostImageSerializer
from apps.post.models import Post,PostImage
from apps.stories.permissions import IsOwner


class PostApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            return (IsOwner(),permissions.IsAdminUser(), )
        else:
            return (permissions.IsAuthenticated(),)    

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class PostApiViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer





