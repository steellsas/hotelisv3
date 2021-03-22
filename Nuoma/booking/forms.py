from django.forms import ModelForm
from .models import Reservation
from django import forms


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_day', 'end_day']

        # exclude = ['user', 'status']


class AddReserveDayForm(forms.Form):

    start_day = forms.DateField(input_formats=['%Y-%m-%d'])
    end_day = forms.DateField(input_formats=['%Y-%m-%d'])

