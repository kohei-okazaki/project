import logging
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from kintai.forms import LoginForm, UserCreateForm, UserEditForm
from kintai.models import UserData
from kintai.contents.util import date_util
from kintai.contents.dailywork import dailywork_service
from kintai.contents.user import user_service

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

            user_list = UserData.objects.filter(seq_user_id = loginForm.cleaned_data["seq_user_id"], password = loginForm.cleaned_data["password"])
            if (user_list.count() < 1):
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

    def get(self, request):

        current_user = user_service.get_user(request.session["seq_user_id"])
        self.params["form"] = current_user

        return render(request, "user/edit.html", self.params)

    def post(self, request):

        current_user = user_service.get_user(request.session["seq_user_id"])

        user = UserEditForm(request.POST, instance = current_user)
        user.save()

        return redirect(to="user_edit")

# 日次勤怠登録View
class DailyworkCreateView(TemplateView):

    def __init__(self):
        self.params = {
            "business_calendar_mt_list": [],
            "yyyymm_list": [],
            "current_month": ""
        }

    def get(self, request):

        sysdate = date_util.get_sysdate()
        self.params["yyyymm_list"].append(date_util.to_str(sysdate, date_util.format_YYYYMM))
        self.params["yyyymm_list"].append(date_util.to_str(date_util.get_any_month(sysdate, -1), date_util.format_YYYYMM))
        self.params["yyyymm_list"].append(date_util.to_str(date_util.get_any_month(sysdate, -2), date_util.format_YYYYMM))

        # 対象年月を取得
        yyyymm = None
        if "yyyymm" in request.GET:
            yyyymm = request.GET["yyyymm"]

        yyyymm = date_util.get_str_yyyymm(yyyymm)
        self.params["current_month"] = yyyymm
        fromDate = date_util.get_first_date_str(yyyymm)
        toDate = date_util.get_last_date_str(yyyymm)

        # 対象年月の営業日マスタを取得
        self.params["business_calendar_mt_list"] = dailywork_service.get_business_calendar_mt_list(fromDate, toDate)

        return render(request, "dailywork/create.html", self.params)
    
    def post(self, request):

        current_user = UserData.objects.get(seq_user_id=request.session["seq_user_id"])
        dailywork_service.regist_daily_user_work_data(user=current_user, \
            year=request.POST["year"], month=request.POST["month"], day=request.POST["day"], \
            start_hh=request.POST["start_hh"], start_mi=request.POST["start_mi"], \
            end_hh=request.POST["end_hh"], end_mi=request.POST["end_mi"])

        return redirect(to="dailywork_create")