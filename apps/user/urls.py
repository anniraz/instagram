from rest_framework.routers import DefaultRouter

from apps.user.views import UserApiViewSet

router = DefaultRouter()
router.register(
    prefix='user',
    viewset=UserApiViewSet
)

urlpatterns = router.urls

