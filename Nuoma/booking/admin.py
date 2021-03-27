from django.contrib import admin
from .models import Reservation

# Register your models here.
#


@admin.register(Reservation)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'room_id', 'start_day', 'end_day', 'total', 'advance', 'status' ]
    list_editable = ['advance']
