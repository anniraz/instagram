from django.contrib import admin

from apps.user.models import User, UserImage

admin.site.register(User)
admin.site.register(UserImage)
