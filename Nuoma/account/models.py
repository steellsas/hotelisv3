from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.name}'


