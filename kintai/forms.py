from django import forms
from kintai.models import DailyUserWorkData, UserData


class LoginForm(forms.Form):
    '''
    ログインForm
    '''

    # ユーザID
    seq_user_id = forms.IntegerField(required=True, label="ユーザID")
    # パスワード
    password = forms.CharField(required=True, label="パスワード")


class UserCreateForm(forms.ModelForm):
    '''
    ユーザ作成Form
    '''
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]


class UserEditForm(forms.ModelForm):
    '''
    ユーザ設定Form
    '''
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]


class DailyworkCreateForm(forms.ModelForm):
    '''
    日次勤怠登録Form
    '''
    class Meta:
        model = DailyUserWorkData
        fields = ["seq_user_id", "company_cd", "division_cd",
                  "work_start_date", "work_end_date", "actual_work_date"]
