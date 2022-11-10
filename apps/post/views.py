from rest_framework import viewsets

from apps.post.serializers import PostSerializer
from apps.post.models import Post


class PostApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


