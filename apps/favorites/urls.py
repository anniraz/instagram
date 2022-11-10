from rest_framework.routers import DefaultRouter

from apps.favorites.views import FavoriteApiViewSet,FavoriteCategoryApiViewSet

router = DefaultRouter()
router.register(prefix='my',viewset=FavoriteApiViewSet),
router.register(prefix='category',viewset=FavoriteCategoryApiViewSet)
urlpatterns = router.urls
