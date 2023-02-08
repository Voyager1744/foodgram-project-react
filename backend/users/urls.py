from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    # path('auth/', include(authorization)),
    path('', include(router.urls)),
]
