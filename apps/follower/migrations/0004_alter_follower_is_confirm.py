# Generated by Django 4.1.3 on 2022-11-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follower', '0003_follower_is_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='is_confirm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]