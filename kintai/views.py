import logging
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from .forms import LoginForm, UserCreateForm, UserEditForm
from .models import UserData, BusinessCalendarMt
from .contents.util import date_util

logger = logging.getLogger(__name__)


# ログインView
class LoginView(TemplateView):

    def __init__(self):
        self.params = {
            "form": LoginForm()
        }

    def get(self, request):

        # セッション削除
        request.session.flush()

        return render(request, "login/index.html", self.params)
    
    def post(self, request):

        loginForm = LoginForm(request.POST)
        if (loginForm.is_valid()):

            userList = UserData.objects.filter(seq_user_id = loginForm.cleaned_data["seq_user_id"], password = loginForm.cleaned_data["password"])
            if (userList.count() < 1):
                params = {
                    "errorMessage": "ユーザが存在しません"
                }
                return render(request, "login/index.html", params)

            # セッションにユーザIDを保持
            request.session["seq_user_id"] = loginForm.cleaned_data["seq_user_id"]

            return render(request, "index.html")
    
        return render(request, "login/index.html")

# TOP画面View
class TopView(TemplateView):

    def get(self, request):
        if ("seq_user_id" in request.session) :
            return render(request, "index.html")
        return render(request, "login/index.html")

# ユーザ作成View
class UserCreateView(CreateView):
    template_name = "user/create.html"
    form_class = UserCreateForm
    success_url ="/kintai/login"

# ユーザ編集View
class UserEditView(TemplateView):

    def __init__(self):
        self.params = {
            "form": UserEditForm()
        }
    
    def getUserData(self, seq_user_id):
        return UserData.objects.get(seq_user_id=seq_user_id)

    def get(self, request):

        currentUser = self.getUserData(request.session["seq_user_id"])
        self.params["form"] = currentUser

        return render(request, "user/edit.html", self.params)

    def post(self, request):

        currentUser = self.getUserData(request.session["seq_user_id"])

        user = UserEditForm(request.POST, instance = currentUser)
        user.save()

        return redirect(to="user_edit")

# 日次勤怠登録View
class DailyworkCreateView(TemplateView):

    def __init__(self):
        self.params = {
            "businessCalendarMtList": []
        }

    def get(self, request):

        # 対象年月を取得
        yyyymm = None
        if "yyyymm" in request.GET:
            yyyymm = request.GET["yyyymm"]

        yyyymm = date_util.getStrYYYYMM(yyyymm)
        fromDate = date_util.getFirstDateForStr(yyyymm)
        toDate = date_util.getLastDateForStr(yyyymm)

        # 対象年月の営業日マスタを取得
        businessCalendarMtList = BusinessCalendarMt.objects.filter(date__range=[fromDate, toDate])
        self.params["businessCalendarMtList"] = businessCalendarMtList

        return render(request, "dailywork/create.html", self.params)