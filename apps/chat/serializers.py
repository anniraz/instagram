from apps.user.models import User
from rest_framework import serializers
from apps.chat.models import Message

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Message
        fields = ['id','sender','receiver', 'message', 'timestamp','is_read']
        read_only_fields = ('sender','receiver','is_read',)


