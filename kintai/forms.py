from django import forms
from kintai.models import UserData


class LoginForm(forms.Form):
    '''
    ログインForm
    '''

    # ユーザID
    seq_user_id = forms.IntegerField(required=True, label="ユーザID")
    # パスワード
    password = forms.CharField(required=True, label="パスワード")


class UserCreateForm(forms.Form):
    '''
    ユーザ作成Form
    '''
    # パスワード
    password = forms.CharField(required=True, label="パスワード")
    # 企業コード
    company_cd = forms.CharField(required=True, max_length=5, label="企業コード")
    # 部署コード
    division_cd = forms.CharField(required=True, max_length=5, label="部署コード")


class UserEditForm(forms.ModelForm):
    '''
    ユーザ設定Form
    '''
    class Meta:
        model = UserData
        fields = ["password", "company_cd", "division_cd"]


class DailyworkCreateForm(forms.Form):
    '''
    日次勤怠登録Form
    '''
    # 対象年
    year = forms.CharField(required=True, label="対象年")
    # 対象月
    month = forms.CharField(required=True, label="対象月")
    # 対象日
    day = forms.CharField(required=True, label="対象日")
    # 作業開始(時)
    start_hh = forms.CharField(required=True, label="作業開始(時)")
    # 作業開始(分)
    start_mi = forms.CharField(required=True, label="作業開始(分)")
    # 作業終了(時)
    end_hh = forms.CharField(required=True, label="作業終了(時)")
    # 作業終了(分)
    end_mi = forms.CharField(required=True, label="作業終了(分)")
