from django.db.models import Q

from rest_framework.decorators import action
from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.user.models import User                                
from apps.chat.models import Message                                                 
from apps.chat.serializers import MessageSerializer,MessageListSerializer

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
        messages=Message.objects.filter(Q(sender=owner,receiver_id=User.objects.get(id=pk))|Q(sender=User.objects.get(id=pk),receiver_id=owner) )
        serializer=MessageSerializer(messages,many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        receiver=User.objects.get(id=pk)
        return serializer.save(sender=self.request.user,receiver=receiver)






