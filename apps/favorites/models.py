from django.db import models


from apps.post.models import Post
from apps.user.models import User

class FavoriteCategory(models.Model):
    title=models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='favorite_category_user', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} {self.user.username}'

class Favorite(models.Model):
    category=models.ForeignKey(FavoriteCategory,on_delete=models.CASCADE,null=True,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE ,related_name='post')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title}'

    class Meta:
        unique_together = (('post', 'user',),)
