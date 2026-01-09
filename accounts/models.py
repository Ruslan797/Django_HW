from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомный пользователь.
    Сейчас расширения нет, но модель своя (под ДЗ и будущие поля).
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

