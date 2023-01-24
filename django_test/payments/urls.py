from rest_framework.routers import DefaultRouter

from .views import PaymentModelViewSet

router = DefaultRouter()
router.register(r"", PaymentModelViewSet, basename="players")

urlpatterns = router.urls
