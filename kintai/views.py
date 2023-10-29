import datetime
import logging
from urllib.parse import urlencode
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from kintai.contents.util.dto import UserDataDto
from kintai.forms import DailyworkCreateForm, LoginForm, UserCreateForm, UserEditForm
from kintai.contents.util import date_util
from kintai.contents.dailywork import dailywork_service
from kintai.contents.user import user_service
from kintai.contents.mt import company_mt_service, division_mt_service

# Logger
logger: logging.Logger = logging.getLogger(__name__)


class LoginView(TemplateView):
    """ログインView

    Args:
        TemplateView (_type_): テンプレートView

    Returns:
        HttpResponse: レスポンス情報
    """

    def __init__(self):
        self.params = {
            "success_message": None,
            "warn_message": None,
            "error_message": None,
        }

    def get(self, request: HttpRequest) -> HttpResponse:

        # セッション削除
        request.session.flush()

        if "is_success" in request.GET:
            self.params["success_message"] = "登録完了しました"

        return render(request, "login/index.html", self.params)

    def post(self, request: HttpRequest) -> HttpResponse:

        loginForm: LoginForm = LoginForm(request.POST)
        if (loginForm.is_valid()):

            dto: UserDataDto = UserDataDto()
            dto.seq_user_id = loginForm.cleaned_data["seq_user_id"]
            dto.password = loginForm.cleaned_data["password"]
            dto_list = user_service.get_user_by_id_and_password(dto)

            if len(dto_list) < 1:
                params = {
                    "warn_message": "ユーザが存在しません"
                }
                return render(request, "login/index.html", params)

            # セッションにユーザIDを保持
            request.session["seq_user_id"] = loginForm.cleaned_data["seq_user_id"]

            return render(request, "index.html")

        return render(request, "login/index.html")


class TopView(TemplateView):
    """TOP画面View

    Args:
        TemplateView (_type_): テンプレートView

    Returns:
        HttpResponse: レスポンス情報
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        if ("seq_user_id" in request.session):
            return render(request, "index.html")
        return render(request, "login/index.html")


class UserCreateView(TemplateView):
    """ユーザ作成View

    Args:
        TemplateView (_type_): テンプレートView

    Returns:
        HttpResponse: レスポンス情報
    """

    def __init__(self):
        self.params = {
            "form": UserCreateForm(),
            "company_mt_list": [],
            "division_mt_list": [],
            "success_message": None,
            "warn_message": None,
            "error_message": None,
        }

    def get(self, request: HttpRequest) -> HttpResponse:

        # 企業マスタリストを取得
        self.params["company_mt_list"] = company_mt_service.get_dto_list(
            "company_cd")
        # 部署マスタリストを取得
        self.params["division_mt_list"] = division_mt_service.get_dto_list(
            "division_cd")

        return render(request, "user/create.html", self.params)

    def post(self, request: HttpRequest) -> HttpResponse:

        form: UserCreateForm = UserCreateForm(request.POST)
        if form.is_valid():
            dto: UserDataDto = UserDataDto()
            dto.password = form.cleaned_data["password"]
            dto.company_cd = form.cleaned_data["company_cd"]
            dto.division_cd = form.cleaned_data["division_cd"]
            user_service.regist_user(dto)

            redirect_url = reverse("login")
            parameters = urlencode({"is_success": True})
            url = f"{redirect_url}?{parameters}"
            return redirect(url)

        else:
            self.params["error_message"] = "登録に失敗しました"
            return render(request, "user/create.html", self.params)


class UserEditView(TemplateView):
    """ユーザ編集View

    Args:
        TemplateView (_type_): テンプレートView

    Returns:
        HttpResponse: レスポンス情報
    """

    def __init__(self):
        self.params = {
            "form": UserEditForm(),
            "success_message": None,
            "warn_message": None,
            "error_message": None,
        }

    def get(self, request: HttpRequest) -> HttpResponse:

        current_user: UserDataDto = user_service.get_user_data_dto(
            request.session["seq_user_id"])

        self.params["form"] = current_user

        if "is_success" in request.GET:
            self.params["success_message"] = "登録完了しました"

        return render(request, "user/edit.html", self.params)

    def post(self, request: HttpRequest) -> HttpResponse:

        form: UserEditForm = UserEditForm(request.POST)
        if form.is_valid():
            current_user: UserDataDto = user_service.get_user_data_dto(
                request.session["seq_user_id"])
            current_user.password = form.cleaned_data["password"]
            user_service.update_user(current_user)

            redirect_url = reverse("user_edit")
            parameters = urlencode({"is_success": True})
            url = f"{redirect_url}?{parameters}"
            return redirect(url)

        return redirect(to="user_edit")


class DailyworkCreateView(TemplateView):
    """日次勤怠登録View

    Args:
        TemplateView (_type_): テンプレートView

    Returns:
        HttpResponse: レスポンス情報
    """

    def __init__(self):
        self.params = {
            "dto_list": [],
            "yyyymm_list": [],
            "current_month": "",
            "success_message": None,
            "warn_message": None,
            "error_message": None,
        }

    def get(self, request: HttpRequest) -> HttpResponse:

        sysdate: datetime = date_util.get_sysdate()
        self.params["yyyymm_list"].append(
            date_util.to_str(sysdate, date_util.FORMAT_YYYYMM))
        self.params["yyyymm_list"].append(date_util.to_str(
            date_util.get_any_month(sysdate, -1), date_util.FORMAT_YYYYMM))
        self.params["yyyymm_list"].append(date_util.to_str(
            date_util.get_any_month(sysdate, -2), date_util.FORMAT_YYYYMM))

        # 対象年月を取得
        yyyymm: str = None
        if "yyyymm" in request.GET:
            yyyymm = request.GET["yyyymm"]

        yyyymm: str = date_util.get_str_yyyymm(yyyymm)
        user: UserDataDto = user_service.get_user_data_dto(
            seq_user_id=request.session["seq_user_id"])

        self.params["current_month"] = yyyymm
        self.params["dto_list"] = dailywork_service.get_daily_user_work_dto_list(
            user=user, yyyymm=yyyymm)

        if "is_success" in request.GET:
            self.params["success_message"] = "登録完了しました"

        return render(request, "dailywork/create.html", self.params)

    def post(self, request: HttpRequest) -> HttpResponse:

        form: DailyworkCreateForm = DailyworkCreateForm(request.POST)

        if form.is_valid():
            user: UserDataDto = user_service.get_user_data_dto(
                seq_user_id=request.session["seq_user_id"])
            dailywork_service.regist_daily_user_work_data(user, form)

            redirect_url = reverse("dailywork_create")
            parameters = urlencode({"is_success": True})
            url = f"{redirect_url}?{parameters}"
            return redirect(url)

        else:
            self.params["error_message"] = "登録に失敗しました"

            sysdate: datetime = date_util.get_sysdate()
            self.params["yyyymm_list"].append(
                date_util.to_str(sysdate, date_util.FORMAT_YYYYMM))
            self.params["yyyymm_list"].append(date_util.to_str(
                date_util.get_any_month(sysdate, -1), date_util.FORMAT_YYYYMM))
            self.params["yyyymm_list"].append(date_util.to_str(
                date_util.get_any_month(sysdate, -2), date_util.FORMAT_YYYYMM))
            self.params["current_month"] = request.POST["yyyymm"]
            user: UserDataDto = user_service.get_user_data_dto(
                seq_user_id=request.session["seq_user_id"])
            self.params["dto_list"] = dailywork_service.get_daily_user_work_dto_list(
                user=user, yyyymm=self.params["current_month"])

            return render(request, "dailywork/create.html", self.params)
