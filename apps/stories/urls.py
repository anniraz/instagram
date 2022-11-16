from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.stories.views import *

router = DefaultRouter()
router.register(prefix='',viewset=StoriesApiViewSet)


urlpatterns = [
    path('archive/',ArchiveApiView.as_view()),
    path('archive/<int:pk>/',MyArchiveApiView.as_view())

]


urlpatterns += router.urls
