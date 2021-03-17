from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_day', 'end_day', 'user_id', 'room_id', 'total', 'advance']

        # exclude = ['user', 'status']

