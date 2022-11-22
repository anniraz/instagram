from rest_framework import serializers

from apps.follower.models import Follower

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id','from_user','to_user','create_at','is_confirm',)
        read_only_fields = ( 'from_user','is_confirm',)


    def create(self, validated_data):
        if validated_data['to_user'].is_private==False:
            validated_data['is_confirm']=True
        return super().create(validated_data)

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id','from_user','to_user','create_at','is_confirm',)
        read_only_fields = ( 'from_user','is_confirm',)
    
class ConfirmFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id','create_at','is_confirm',)
