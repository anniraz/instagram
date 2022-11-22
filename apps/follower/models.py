from django.db import models
from apps.user.models import User


class Follower(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    is_confirm=models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return f"{self.create_at}"

    class Meta:
        ordering = ('-create_at',)
        unique_together = (('from_user', 'to_user',),)
