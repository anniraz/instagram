from rest_framework import viewsets,permissions

from apps.post.serializers import PostSerializer,PostImageSerializer
from apps.post.models import Post,PostImage
from apps.user.permissions import IsOwner,IsPostOwner


class PostApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)    

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class PostImageApiViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsPostOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  





