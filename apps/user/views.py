from rest_framework import viewsets,permissions

from apps.user.models import User,UserImage
from apps.stories.permissions import IsOwnerUser,IsOwner
from apps.user.serializers import UserSerializerList,UserImageSerializer


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerList

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsOwnerUser(),)
        else:
            return (permissions.AllowAny(),) 


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