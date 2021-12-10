from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import CategoryLog, ReviewLog


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CategoryLogForm(forms.ModelForm):
    class Meta:
        model = CategoryLog
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewLog
        fields = '__all__'