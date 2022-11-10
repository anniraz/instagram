from django.db import models


from apps.post.models import Post
from apps.user.models import User



class Favorite(models.Model):
    
    post=models.ForeignKey(Post,on_delete=models.CASCADE ,related_name='post')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title}'

    class Meta:
        unique_together = (('post', 'user',),)
