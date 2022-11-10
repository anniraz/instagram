from rest_framework import serializers

from apps.favorites.models import Favorite,FavoriteCategory


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('category','post','user',)
        read_only_fields = ("id", 'user',)

class FavoriteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCategory
        fields = ('id','title','user',)
        read_only_fields = ('user',)