from rest_framework.routers import DefaultRouter

from apps.post.views import PostApiViewSet,PostImageApiViewSet

router = DefaultRouter()
router.register(prefix='all',viewset=PostApiViewSet)
router.register(prefix='image',viewset=PostImageApiViewSet)

urlpatterns = router.urls
