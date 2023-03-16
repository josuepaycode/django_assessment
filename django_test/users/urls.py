from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from users.views import AuthToken, login_user, logout_user

router = DefaultRouter()

urlpatterns = [
    path(r'', include(router.urls)),
    path('api-token-auth/', AuthToken.as_view()),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]