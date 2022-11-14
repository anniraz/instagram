from django.urls import path
from .views import *


urlpatterns = [
    path('send/<int:pk>/',SendMessageApiView.as_view()),

]