from rest_framework import viewsets

from apps.user.models import User
from apps.user.serializers import UserSerializerList


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerList
