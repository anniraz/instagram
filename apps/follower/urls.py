from rest_framework.routers import DefaultRouter

from apps.follower.views import FollowerApiViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=FollowerApiViewSet
)
urlpatterns = router.urls
