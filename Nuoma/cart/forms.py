from django import forms


class CartAddRoomForm(forms.Form):

    start_day = forms.DateField(input_formats=['%Y-%m-%d'])
    end_day = forms.DateField(input_formats=['%Y-%m-%d'])


#
# class CartAddRoomForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     moth = forms. CharField(max_length=10)
#     override = forms.BooleanField(required=False,
#                                   initial=False,
#                                   widget=forms.HiddenInput)
