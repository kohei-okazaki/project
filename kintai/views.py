from django.shortcuts import redirect, render
from .forms import UserCreateForm, UserEditForm
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
    # ユーザ一覧
    users = UserData.objects.all()
    params = {
        "users": users
    }
    return render(request, "user/list.html", params)


def user_create(request):
    # ユーザ作成
    if (request.method == "GET") :
        params = {
            "form": UserCreateForm()
        }
    else:
        obj = UserData()
        user = UserCreateForm(request.POST, instance = obj)
        user.save()
        return redirect(to="login")

    return render(request, "user/create.html", params)

def user_edit(request, input_seq_user_id):
    # ユーザ編集
    oldUser = UserData.objects.get(seq_user_id=input_seq_user_id)
    if (request.method == "POST") :
        user = UserEditForm(request.POST, instance = oldUser)
        user.save()
        return redirect("user/edit/" + input_seq_user_id)
    
    params = {
        "seqUserId": input_seq_user_id,
        "form": UserEditForm(instance = oldUser),
    }

    return render(request, "user/edit.html", params)