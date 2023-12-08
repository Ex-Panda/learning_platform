from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    first_name = models.CharField(_("first name"), max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(verbose_name='email', unique=True)
    phone = models.IntegerField(verbose_name='телефон', unique=True, **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(verbose_name='аватар', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


