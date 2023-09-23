import datetime
import logging
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from kintai.forms import LoginForm, UserCreateForm, UserEditForm
from kintai.contents.util import date_util
from kintai.contents.dailywork import dailywork_service
from kintai.contents.user import user_service
from kintai.models import UserData

logger = logging.getLogger(__name__)


class LoginView(TemplateView):
    '''
    ログインView
    '''

    def __init__(self):
        self.params = {
            "form": LoginForm()
        }

    def get(self, request: HttpRequest) -> HttpResponse:

        # セッション削除
        request.session.flush()

        return render(request, "login/index.html", self.params)

    def post(self, request: HttpRequest) -> HttpResponse:

        loginForm: LoginForm = LoginForm(request.POST)
        if (loginForm.is_valid()):

            user_list = user_service.get_user_by_id_and_password(
                loginForm.cleaned_data["seq_user_id"], loginForm.cleaned_data["password"])
            if (user_list.count() < 1):
                params = {
                    "errorMessage": "ユーザが存在しません"
                }
                return render(request, "login/index.html", params)

            # セッションにユーザIDを保持
            request.session["seq_user_id"] = loginForm.cleaned_data["seq_user_id"]

            return render(request, "index.html")

        return render(request, "login/index.html")


class TopView(TemplateView):
    '''
    TOP画面View
    '''

    def get(self, request: HttpRequest) -> HttpResponse:
        if ("seq_user_id" in request.session):
            return render(request, "index.html")
        return render(request, "login/index.html")


class UserCreateView(CreateView):
    '''
    ユーザ作成View
    '''
    template_name = "user/create.html"
    form_class = UserCreateForm
    success_url = "/kintai/login"


class UserEditView(TemplateView):
    '''
    ユーザ編集View
    '''

    def __init__(self):
        self.params = {
            "form": UserEditForm()
        }

    def get(self, request: HttpRequest) -> HttpResponse:

        current_user: UserData = user_service.get_user(
            request.session["seq_user_id"])

        self.params["form"] = current_user

        return render(request, "user/edit.html", self.params)

    def post(self, request: HttpRequest) -> HttpResponse:

        current_user: UserData = user_service.get_user(
            request.session["seq_user_id"])

        user: UserEditForm = UserEditForm(request.POST, instance=current_user)
        user.save()

        return redirect(to="user_edit")


class DailyworkCreateView(TemplateView):
    '''
    日次勤怠登録View
    '''

    def __init__(self):
        self.params = {
            "business_calendar_mt_list": [],
            "yyyymm_list": [],
            "current_month": ""
        }

    def get(self, request: HttpRequest) -> HttpResponse:

        sysdate: datetime = date_util.get_sysdate()
        self.params["yyyymm_list"].append(
            date_util.to_str(sysdate, date_util.format_YYYYMM))
        self.params["yyyymm_list"].append(date_util.to_str(
            date_util.get_any_month(sysdate, -1), date_util.format_YYYYMM))
        self.params["yyyymm_list"].append(date_util.to_str(
            date_util.get_any_month(sysdate, -2), date_util.format_YYYYMM))

        # 対象年月を取得
        yyyymm: str = None
        if "yyyymm" in request.GET:
            yyyymm = request.GET["yyyymm"]

        yyyymm: str = date_util.get_str_yyyymm(yyyymm)
        self.params["current_month"] = yyyymm
        from_date: datetime = date_util.get_first_date_str(yyyymm)
        to_date: datetime = date_util.get_last_date_str(yyyymm)

        # 対象年月の営業日マスタを取得
        self.params["business_calendar_mt_list"] = dailywork_service.get_business_calendar_mt_list(
            from_date, to_date)

        return render(request, "dailywork/create.html", self.params)

    def post(self, request: HttpRequest) -> HttpResponse:

        current_user: UserData = user_service.get_user(
            seq_user_id=request.session["seq_user_id"])
        dailywork_service.regist_daily_user_work_data(user=current_user,
                                                      year=request.POST["year"], month=request.POST["month"], day=request.POST["day"],
                                                      start_hh=request.POST["start_hh"], start_mi=request.POST["start_mi"],
                                                      end_hh=request.POST["end_hh"], end_mi=request.POST["end_mi"])

        return redirect(to="dailywork_create")
