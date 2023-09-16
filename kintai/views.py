import logging
from django.shortcuts import redirect, render
from .forms import LoginForm, UserCreateForm, UserEditForm
from .models import UserData

logger = logging.getLogger(__name__)

# ログイン
def login(request):

    # セッション削除
    request.session.flush()
    params = {
        "form": LoginForm()
    }

    return render(request, "login/index.html", params)

# ログイン後のメニュー
def index(request):

    if ("seq_user_id" in request.session) :
        # ログイン済の場合
        logger.info(request.session["seq_user_id"])
        return render(request, "index.html")

    if (request.method == "GET") :
        return render(request, "login/index.html")
    
    # USER_DATAを検索し、対象のユーザが登録されているか確認する
    seq_user_id = request.POST["seq_user_id"]
    password = request.POST["password"]
    userList = UserData.objects.filter(seq_user_id = seq_user_id, password = password)

    if (userList.count()):
        params = {
            "errorMessage": "ユーザが存在しません"
        }
        return render(request, "login/index.html", params)

    # セッションにユーザIDを保持
    request.session["seq_user_id"] = seq_user_id

    return render(request, "index.html")


# ユーザ作成
def user_create(request):

    if (request.method == "GET") :
        params = {
            "form": UserCreateForm()
        }
        return render(request, "user/create.html", params)
    
    obj = UserData()
    user = UserCreateForm(request.POST, instance = obj)
    user.save()

    return redirect(to="login")

# ユーザ編集
def user_edit(request):

    sessionSeqUserId = request.session["seq_user_id"]
    currentUser = UserData.objects.get(seq_user_id=sessionSeqUserId)

    if (request.method == "GET") :
    
        params = {
            "form": UserEditForm(instance = currentUser),
        }

        return render(request, "user/edit.html", params)

    
    user = UserEditForm(request.POST, instance = currentUser)
    user.save()
    return redirect(to="user_edit")
