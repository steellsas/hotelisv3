from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('description', 'phone')


STATUS_CHOICES = (
    ("1", "Patvirtinti"),
    ("2", "Apmoketa"),
    ("-1", "At6aukta"),
    ("4", "Atvyko"),

)
class ChangeStatus(forms.Form):
    reservation_status = forms.TypedChoiceField(choices=STATUS_CHOICES)

