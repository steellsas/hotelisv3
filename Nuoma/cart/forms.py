from django import forms


# add start_day and End_day to the cart
class CartAddRoomForm(forms.Form):
    start_day = forms.DateField()
    end_day = forms.DateField()
