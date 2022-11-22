from rest_framework import viewsets,permissions

from apps.user.models import User,UserImage
from apps.user.permissions import IsOwnerUser,IsOwner
from apps.user.serializers import UserSerializerList,UserImageSerializer,UserSerializer,MySerializerList


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerList

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsOwnerUser(),)
        else:
            return (permissions.AllowAny(),)


    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializerList
        elif self.action in ['update', 'partial_update', 'destroy',]:
            return MySerializerList
        return UserSerializer


class UserProfilePhotoApiView(viewsets.ModelViewSet):
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsOwner(),)
        else:
            return (permissions.AllowAny(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)