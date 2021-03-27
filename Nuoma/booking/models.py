from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from rooms.models import Room



auth_user = settings.AUTH_USER_MODEL if getattr(
    settings, "AUTH_USER_MODEL") else User


class Reservation(models.Model):


    STATUS =(
        (0, "Builded"),
        (1, "Accepted"),
        (3, "Canceled"),
        (4, "Paid"),
        (5, "Confirmed"),
        (6,  "Ended"),
    )

    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    total = models.DecimalField(max_digits=5, null=True, decimal_places=2)
    advance = models.DecimalField(max_digits=5, null=True,decimal_places=2)
    status = models.SmallIntegerField(choices=STATUS, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"  {self.get_status_display()}  ({self.start_day} to {self.end_day})"




