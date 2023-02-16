from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UsersViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UsersViewSet)

urlpatterns = [
    # path('auth/', include(authorization)),
    path('', include(router.urls)),
]
