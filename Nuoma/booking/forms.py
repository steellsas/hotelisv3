from django.forms import ModelForm
from .models import Reservation
from django import forms


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_day', 'end_day']

        # exclude = ['user', 'status']


class AddReserveDayForm(forms.Form):

    # start_day = forms.DateField(input_formats = ['%Y-%m-%d'])
    # end_day = forms.DateField(input_formats = ['%Y-%m-%d'])
     date_range = forms.CharField(max_length=50)


class TestEmailForm(forms.Form):

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)


class AddReserveDayRangeForm(forms.Form):
    date_range = forms.DateField(input_formats = ['%Y-%m-%d'])
