import datetime
from django.utils import timezone

from instagram_rest.celery import app
from apps.stories.models import Stories,Archive

# video=models.FileField(upload_to='archive/',null=True,blank=True)
#     photo=models.ImageField(upload_to='archive/',null=True,blank=True)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     created_a

@app.task
def stories():
    today=timezone.now()
    for i in Stories.objects.all():
        create_date=i.created_at+timezone.timedelta(hours=24)
        if create_date<=today:
            archive=Archive.objects.create(
                video=i.video,
                photo=i.photo,
                user=i.user
            )
            
            i.delete()

