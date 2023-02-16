from django.contrib import admin
from django.urls import include, path

api = [
    path('', include('users.urls', namespace='users')),
    path('', include('recipes.urls', namespace='recipes')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]
