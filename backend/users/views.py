from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, UsersSerializer

User = get_user_model()


class UsersViewSet(UserViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()



