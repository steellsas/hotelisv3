from django import forms


class CartAddRoomForm(forms.Form):

    start_day = forms.DateField(input_formats=['%Y-%m-%d'])
    end_day = forms.DateField(input_formats=['%Y-%m-%d'])


