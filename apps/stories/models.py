from django.db import models
import datetime
from apps.user.models import User


class Stories(models.Model):
    video=models.FileField(upload_to='stories/',null=True,blank=True)
    photo=models.ImageField(upload_to='stories/',null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'