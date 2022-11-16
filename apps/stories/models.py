from django.db import models
from apps.user.models import User
from django.utils import timezone


class Stories(models.Model):
    video=models.FileField(upload_to='stories/',null=True,blank=True)
    photo=models.ImageField(upload_to='stories/',null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} {self.created_at}'

class Archive(models.Model):
    video=models.FileField(upload_to='archive/',null=True,blank=True)
    photo=models.ImageField(upload_to='archive/',null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} {self.created_at}'   