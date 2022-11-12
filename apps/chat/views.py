from django.db.models import Q

from rest_framework import generics,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.user.models import User                                
from apps.chat.models import Message                                                 
from apps.chat.serializers import MessageSerializer 

class SendMessageApiView(generics.ListCreateAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,pk):
        owner=request.user
        messages=Message.objects.filter(Q(sender=owner,receiver_id=User.objects.get(id=pk))|Q(sender=User.objects.get(id=pk),receiver_id=owner) )
        serializer=MessageSerializer(messages,many=True)
        return Response(serializer.data)
    # def post(self, request, pk):
    #     if request.data['receiver']==str(request.user.id):
    #         return Response({'error': 'Не отправляй сообщение самому себе'})
    #     print('================================')
    #     print(request.data['receiver'])
    #     # request.data['receiver']=User.objects.get(id=pk)
    #     return super().post(request)
        
    # def get_queryset(self):
    #     owner=self.request.user
    #     return Message.objects.filter(sender=owner)


    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        receiver=User.objects.get(id=pk)
        return serializer.save(sender=self.request.user,receiver=receiver)




class GetMessageApiView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk):
        owner=request.user
        messages=Message.objects.filter(sender=owner,receiver_id=User.objects.get(id=pk))
        serializer=MessageSerializer(messages,many=True)
        return Response(serializer.data)
    
    # def post(self,request,pk):
    #     owner=request.user
    #     new_message=Message.objects.create(
    #         sender=owner,
    #         receiver=User.objects.get(id=pk),
    #         message=request.data["message"]
    #     )
    #     return Response({"new":model_to_dict(new_message)})


