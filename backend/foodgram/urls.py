from django.contrib import admin
from django.urls import include, path

api = [
    path('', include('api.urls', namespace='api')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]
