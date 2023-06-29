from django import forms
from .models import Student, Course

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=25)
    surname = forms.CharField(label='surname', max_length=25)
    email = forms.CharField(label='email', max_length=100)