from rest_framework.response import Response
from rest_framework import viewsets,permissions,generics

from apps.stories.models import Stories,Archive
from apps.stories.serializers import StoriesSerializer,ArchiveSerializer
from apps.user.permissions import IsOwner
from apps.follower.models import Follower

class StoriesApiViewSet(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            return (IsOwner(), )
        else:
            return (permissions.AllowAny(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        owner=request.user
        stories=Stories.objects.all()
        all_followers=Follower.objects.all()
        unfollowers=[]
        
        for i in stories:
            if len(all_followers)==0:
                if i.user != owner:
                    unfollowers.append(i.id)
            else:
                for follower in all_followers:
                    if i.user == follower.to_user and owner==follower.from_user or i.user==owner:
                        pass
                    else:
                        unfollowers.append(i.id)

        queryset=Stories.objects.all().exclude(id__in=unfollowers)
        serializer=StoriesSerializer(queryset,many=True)
        return Response(serializer.data)



class ArchiveApiView(generics.ListAPIView):
    serializer_class = ArchiveSerializer
    permission_classes=[IsOwner]

    def get_queryset(self):
        return Archive.objects.filter(user=self.request.user)

class MyArchiveApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArchiveSerializer
    permission_classes=[IsOwner]

    def get_queryset(self):
        return Archive.objects.filter(user=self.request.user)






