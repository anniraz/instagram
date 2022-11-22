# Generated by Django 4.1.3 on 2022-11-21 05:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0006_alter_postslike_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_read',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]