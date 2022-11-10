from rest_framework.routers import DefaultRouter

from apps.stories.views import StoriesApiViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=StoriesApiViewSet
)
urlpatterns = router.urls