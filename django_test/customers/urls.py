from rest_framework.routers import DefaultRouter

from .views import CustomerModelViewSet

router = DefaultRouter()
router.register(r"", CustomerModelViewSet, basename="players")

urlpatterns = router.urls
