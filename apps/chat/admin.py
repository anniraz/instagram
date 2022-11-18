from django.contrib import admin
from apps.chat.models import Message,GroupChatSettings,GroupMembers,GroupMessages

admin.site.register(Message)
admin.site.register(GroupChatSettings)
admin.site.register(GroupMembers)
admin.site.register(GroupMessages)