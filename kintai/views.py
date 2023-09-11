from django.shortcuts import redirect, render
from .forms import UserCreateForm
from .models import UserData


def login(request):
    # ログイン
    return render(request, "login/index.html")


def index(request):
    # ログイン後のメニュー

    params = {
        "seq_user_id": request.POST["seq_user_id"],
        "password": request.POST["password"],
    }
    return render(request, "index.html", params)


def user_list(request):
    # ユーザの一覧
    users = UserData.objects.all()
    params = {
        "users": users
    }
    return render(request, "user/list.html", params)


def user_create(request):
    # ユーザ作成
    params = {
        "form": UserCreateForm()
    }

    if (request.method == "POST"):
        input_password = request.POST["password"]
        input_company_cd = request.POST["company_cd"]
        user = UserData(password=input_password, company_cd=input_company_cd)
        user.save()
        return redirect(to="login")

    return render(request, "user/create.html", params)
