from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = CharField(max_length=100, required=True,
                         widget=TextInput(attrs={"class": "form-control"}))  # blank=True,
    first_name = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))  # blank=True,
    last_name = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))  # blank=True,
    email = EmailField(max_length=100, widget=EmailInput(attrs={"class": "form-control"}))
    password1 = CharField(min_length=6, max_length=12, required=True,
                          widget=PasswordInput(attrs={"class": "form-control"}))
    password2 = CharField(min_length=6, max_length=12, required=True,
                          widget=PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = CharField(max_length=100, required=True, widget=TextInput(attrs={"class": "form-control"}))
    password = CharField(max_length=12, min_length=6, required=True,
                         widget=PasswordInput(attrs={"class": "form-control"}))
    # password = CharField()

    class Meta:
        model = User
        fields = ("username", "password")