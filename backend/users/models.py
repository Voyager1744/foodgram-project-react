from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    email: str = models.EmailField('Email', max_length=150, unique=True)
    username: str = models.CharField('Логин', max_length=150, unique=True)
    first_name: str = models.CharField('Имя', max_length=150, blank=True)
    last_name: str = models.CharField('Фамилия', max_length=150, blank=True)
    password: str = models.CharField('Пароль', max_length=128)
    is_superuser: bool = models.BooleanField('Администратор', default=False)
    is_active: bool = models.BooleanField('Активный', default=True)

    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    """Модель подписчика."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор рецепта',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_follow',
            ),
        )

    def __str__(self):
        return f'{self.user} подписан на {self.author}.'
