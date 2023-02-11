from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""
    is_subscribed = SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed'
                  )
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }

    def get_is_subscribed(self, obj):
        """
Проверяет подписан ли пользователь
        :param obj: User
        :return: True or False
        """
        user = self.context['request'].user
        return user.is_authenticated  # TODO Дописать условие подписки!
