from rest_framework import routers
from .views import customerViewSet, paymentsViewSet,userViewSet,groupSerializer

router=routers.DefaultRouter()

router.register('api/customers',customerViewSet,'customerapi')
router.register('api/payments',paymentsViewSet,'paymentsapi')
router.register('api/users',userViewSet,'userapi')


urlpatterns=router.urls
