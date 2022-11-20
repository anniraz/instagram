from rest_framework import serializers

from apps.post.models import Post, PostImage,PostsLike

class PostLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostsLike
        fields = '__all__'
        read_only_fields = ('id', 'user',)


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
    post_for_like = PostLikeSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'user',
                  'post_images',
                  'post_for_like',
                  )

        read_only_fields = ('id', 'user', 'create_at')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["like's count"] = instance.post_for_like.count()

        return representation

