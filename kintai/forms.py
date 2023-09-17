from django import forms
from .models import UserData


# ログインForm
class LoginForm(forms.Form):

    # ユーザID
    seq_user_id = forms.IntegerField(required=True, label="ユーザID")
    # パスワード
    password = forms.CharField(required=True, label="パスワード")

# ユーザ作成Form
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]

# ユーザ設定Form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]
