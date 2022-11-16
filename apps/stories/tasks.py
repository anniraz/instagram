import datetime
from django.utils import timezone

from instagram_rest.celery import app
from apps.stories.models import Stories

@app.task
def stories():
    today=timezone.now()
    for i in Stories.objects.all():
        create_date=i.created_at+timezone.timedelta(hours=24)
        if create_date<=today:
            i.delete()

