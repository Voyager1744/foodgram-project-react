from django.contrib import admin
from django.urls import path, include

api = [
    path('', include('users.urls', namespace='users')),
    # path('', include('recipes.urls', namespace='recipes')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]
