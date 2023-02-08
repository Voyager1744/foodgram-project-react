from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField('Email', max_length=150, unique=True)
    username = models.CharField('Логин', max_length=150, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    password = models.CharField('Пароль', max_length=128)
    is_superuser = models.BooleanField('Администратор', default=False)
    is_active = models.BooleanField('Активный', default=True)

    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
