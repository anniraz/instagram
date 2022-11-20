from rest_framework.routers import DefaultRouter

from apps.post.views import PostApiViewSet,PostImageApiViewSet,PostLikeApiView

router = DefaultRouter()
router.register(prefix='all',viewset=PostApiViewSet)
router.register(prefix='image',viewset=PostImageApiViewSet)
router.register(prefix='like',viewset=PostLikeApiView)

urlpatterns = router.urls
