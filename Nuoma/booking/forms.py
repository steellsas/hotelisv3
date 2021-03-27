from django.forms import ModelForm
from .models import Reservation
from django import forms


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_day', 'end_day']

        # exclude = ['user', 'status']


class AddReserveDayForm(forms.Form):

    start_day = forms.DateTimeField(input_formats=['%Y-%m-%d'])
    end_day = forms.DateField(input_formats=['%Y-%m-%d'])


class AuctionForm(forms.Form):
    end_day = forms.DateField()


# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
