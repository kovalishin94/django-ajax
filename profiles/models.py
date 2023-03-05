from django.db import models


class Profile(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        blank=True
    )
    e_mail = models.EmailField(
        max_length=150,
        verbose_name='E-mail',
        blank=True
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'