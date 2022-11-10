from rest_framework import serializers

from apps.stories.models import Stories


class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ('id','user','video','photo','created_at')
        read_only_fields = ( 'user',)