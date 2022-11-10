from rest_framework import viewsets

from apps.comment.serializers import CommentSerializer
from apps.comment.models import Comment


class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
