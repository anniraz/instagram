import datetime

from instagram_rest.celery import app
from apps.stories.models import Stories

@app.task
def stories():
    today=datetime.date.today()
    for i in Stories.objects.all():
        if i.created_at+datetime.timedelta(days=1) == today:
            i.delete()
