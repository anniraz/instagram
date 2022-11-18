from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(prefix='group',viewset=GroupChatSettingsApiView)
router.register(prefix='members',viewset=GroupChatMembersApiView)




urlpatterns = [
    path('messages/<int:pk>/',SendMessageApiView.as_view()),
    path('messages/detail/<int:pk>/',MessagesApiView.as_view()),
    path('group/chat/<int:pk>/',GroupMessagesApiView.as_view())

]

urlpatterns += router.urls
