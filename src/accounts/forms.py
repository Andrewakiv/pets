from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        field = ['username', 'password']

# can use without Meta if inherit from Forms and AuthenticationForm for LoginView


class RegisterForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        labels = {
            'mail': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords is not equal')
        return cd['password2']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    email = forms.CharField(disabled=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'mail': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
        }


class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())
