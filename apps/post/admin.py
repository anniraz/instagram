from django.contrib import admin

from apps.post.models import Post, PostImage

admin.site.register(Post)
admin.site.register(PostImage)

