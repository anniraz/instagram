from django.db import models

from apps.user.models import User


class Message(models.Model):

     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default=False)

     def __str__(self):
           return f'sender: {self.sender} message:{self.message}'

     class Meta:
           ordering = ('timestamp',)



class GroupChatSettings(models.Model):

      owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='chat_owner')
      group_name=models.CharField(max_length=255)
      group_avatar=models.ImageField(upload_to='group_avatars/')

      def __str__(self) -> str:
            return f'{self.owner}: {self.group_name}'      

class GroupMembers(models.Model):
      
      group_room=models.ForeignKey(GroupChatSettings,on_delete=models.CASCADE)
      member=models.ForeignKey(User,on_delete=models.CASCADE,related_name='group_member')
      is_admin=models.BooleanField(default=False)

      def __str__(self) -> str:
            return f'{self.group_room}:member:{self.member}:admin:{self.is_admin}'

class GroupMessages(models.Model):
      chat_room=models.ForeignKey(GroupChatSettings,on_delete=models.CASCADE,related_name='chat_room')
      member=models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_group_member')
      message = models.CharField(max_length=1200)
      timestamp = models.DateTimeField(auto_now_add=True)
      is_read = models.ManyToManyField(User,null=True,blank=True)

      def __str__(self) -> str:
            return f'{self.member}:{self.message}'

