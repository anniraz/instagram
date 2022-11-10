from rest_framework import serializers

from apps.post.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'owner',
                  'update_at',
                  'post_images',
                  )
        read_only_fields = ('id', 'owner', 'create_at')
