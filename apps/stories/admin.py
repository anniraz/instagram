from django.contrib import admin

from apps.stories.models import Stories,Archive
# Register your models here.
admin.site.register(Stories)
admin.site.register(Archive)
