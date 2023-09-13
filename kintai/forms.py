from django.forms.models import ModelForm
from django.forms import Form
from django import forms
from .models import UserData


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["password"]
