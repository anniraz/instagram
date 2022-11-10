from rest_framework.routers import DefaultRouter

from apps.post.views import PostApiViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=PostApiViewSet
)

urlpatterns = router.urls
