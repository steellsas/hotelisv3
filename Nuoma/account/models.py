from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.first_name}'


# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
