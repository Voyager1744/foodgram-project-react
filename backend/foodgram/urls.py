from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from foodgram import settings

api = [
    path('', include('api.urls', namespace='api')),
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
