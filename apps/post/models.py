from django.db import models

from apps.user.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}---{self.user.username}"

    class Meta:
        ordering = ('create_at',)

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.post.title}---{self.post.owner.username}"

    class Meta:
        ordering = ("id",)

