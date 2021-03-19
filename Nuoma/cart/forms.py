from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddRoomForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # day = forms.DateField()
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

#
# class CartAddRoomForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     moth = forms. CharField(max_length=10)
#     override = forms.BooleanField(required=False,
#                                   initial=False,
#                                   widget=forms.HiddenInput)
