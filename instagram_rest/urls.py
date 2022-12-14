from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
   # apps
    path('', include('apps.user.urls')),
    path('post/', include('apps.post.urls')),
    path('comment/', include('apps.comment.urls')),
    path('follower/', include('apps.follower.urls')),
    path('favorite/',include('apps.favorites.urls')),
    path('stories/',include('apps.stories.urls')),
    path('chat/', include('apps.chat.urls')),

    # api
    path('api-auth/', include('rest_framework.urls')),

    # documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]



urlpatterns+=static(settings.MEDIA_URL ,document_root= settings.MEDIA_ROOT)
