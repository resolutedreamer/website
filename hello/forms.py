from django import forms

from .models import Customer

class CustomerForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
