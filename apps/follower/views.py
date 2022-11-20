from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.follower.models import Follower
from apps.follower.serializers import FollowerSerializer,ConfirmFollowingSerializer
from apps.user.models import User

class FollowApiView(generics.CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)


class FollowsApiView(generics.ListAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user=User.objects.get(id=pk)
        return Follower.objects.filter(from_user=user)

class FollowersApiView(generics.ListAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user=User.objects.get(id=pk)
        return Follower.objects.filter(to_user=user)

class UnfollowApiView(generics.DestroyAPIView):
    serializer_class=FollowerSerializer
    queryset = Follower.objects.all()

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        follower=Follower.objects.get(id=pk)
        if follower.from_user==request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'error':'this user is not followed '})

class DeleteFollowerApiView(generics.DestroyAPIView):
    serializer_class=FollowerSerializer
    queryset = Follower.objects.all()

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        follower=Follower.objects.get(id=pk)
        print(follower.from_user)
        if follower.to_user==request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'error':'this user is not your follower'})

class SubscriptionRequestsApiView(generics.ListAPIView):
    serializer_class=FollowerSerializer

    def get_queryset(self):
        if self.request.user.is_private==True:
            return Follower.objects.filter(to_user=self.request.user,is_confirm=False)

class SubscriptionApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ConfirmFollowingSerializer

    def get_queryset(self):
        if self.request.user.is_private==True:
            return Follower.objects.filter(to_user=self.request.user,is_confirm=False)