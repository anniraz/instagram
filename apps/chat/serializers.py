from apps.user.models import User
from rest_framework import serializers
from apps.chat.models import Message,GroupMessages,GroupChatSettings,GroupMembers

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Message
        fields = ['id','sender','receiver', 'message', 'timestamp','is_read']
        read_only_fields = ('sender','receiver','is_read',)

class ChatSettingsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GroupChatSettings
        fields = '__all__'
        read_only_fields=('owner',)


class ChatMembersSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GroupMembers
        fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GroupMessages
        fields='__all__'
        read_only_fields=('member','chat_room','is_read',)






