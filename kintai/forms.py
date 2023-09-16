from django import forms
from .models import UserData


class LoginForm(forms.Form):

    # ユーザID
    seq_user_id = forms.IntegerField(required=True, label="ユーザID")
    # パスワード
    password = forms.CharField(required=True, label="パスワード")

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]
