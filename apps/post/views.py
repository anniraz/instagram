from django.utils import timezone
from rest_framework import viewsets,permissions,generics
from rest_framework.response import Response

from apps.post.serializers import PostSerializer,PostImageSerializer,PostLikeSerializers
from apps.post.models import Post,PostImage,PostsLike,UserReadTime
from apps.follower.models import Follower
from apps.user.models import User
from apps.user.permissions import IsOwner,IsPostOwner


class PostApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)

    def get_queryset(self):
        return Post.objects.filter(user__is_private=False)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class PostImageApiViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsPostOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  


class PostLikeApiView(viewsets.ModelViewSet):
    queryset=PostsLike.objects.all()
    serializer_class=PostLikeSerializers
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class InstagramFeedApiView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user=request.user
        readed_posts=[]
        users=[]
        for i in Follower.objects.filter(from_user=user,is_confirm=True):
            a=i.to_user
            users.append(a)
            for p in Post.objects.filter(user=a):
                read_times=UserReadTime.objects.filter(post=p)
                try:
                    r=read_times.get(user=user)
                    if timezone.now() > (r.read_time + timezone.timedelta(minutes=5)):
                        readed_posts.append(p.id)

                except:
                    read_times.create(post=p,user=user,read_time=timezone.now())

        post=Post.objects.filter(user__in=users).exclude(id__in=readed_posts)
        serializer=PostSerializer(post,many=True)
        return Response(serializer.data)

