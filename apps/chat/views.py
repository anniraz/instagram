from django.db.models import Q

from rest_framework import generics,permissions,viewsets
from rest_framework.response import Response

from apps.user.models import User                                
from apps.chat.models import Message,GroupChatSettings,GroupMembers,GroupMessages                                                 
from apps.chat.serializers import MessageSerializer,ChatSettingsSerializer,ChatMembersSerializer,ChatMessageSerializer
from apps.stories.permissions import IsOwner


class SendMessageApiView(generics.ListCreateAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,pk):
        owner=request.user
        second_user=User.objects.get(id=pk)
        for i in Message.objects.filter(sender=second_user,receiver=owner):
            i.is_read=True
            i.save()
        messages=Message.objects.filter(Q(sender=owner,receiver_id=second_user)|Q(sender=second_user,receiver_id=owner) )
        serializer=MessageSerializer(messages,many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        receiver=User.objects.get(id=pk)
        return serializer.save(sender=self.request.user,receiver=receiver)



class MessagesApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    permission_classes=[IsOwner]

class GroupChatSettingsApiView(viewsets.ModelViewSet):
    queryset=GroupChatSettings.objects.all()
    serializer_class=ChatSettingsSerializer
    # permission_classes=[IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class GroupChatMembersApiView(viewsets.ModelViewSet):
    queryset=GroupMembers.objects.all()
    serializer_class=ChatMembersSerializer

class GroupMessagesApiView(generics.ListCreateAPIView):
    queryset=GroupMessages.objects.all()
    serializer_class=ChatMessageSerializer

    def get(self, request,pk):
        user=request.user
        chat=GroupMessages.objects.filter(chat_room=pk)
        for i in chat:
            if user == i.is_read:
                pass
            i.is_read.add(user)
            i.save()
        serializer=ChatMessageSerializer(chat,many=True)
        return Response(serializer.data)

    def create(self, request,pk, *args, **kwargs):
        members=GroupMembers.objects.filter(group_room=pk)
        user=request.user
        for i in members:
            if user.id == i.member.id:
                return super().create(request,pk, *args, **kwargs)
        return Response({'error':'you are not group member'})

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        chat_room=GroupChatSettings.objects.get(id=pk)
        return serializer.save(member=self.request.user,chat_room=chat_room)





  





