from rest_framework import serializers

from apps.post.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']

class PostSerializer(serializers.ModelSerializer):
    post_images = PostImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'user',
                  'update_at',
                  'post_images',
                  )
        read_only_fields = ('id', 'user', 'create_at')
