from django.shortcuts import redirect, render
from .forms import UserCreateForm, UserEditForm
from .models import UserData
import logging


logger = logging.getLogger(__name__)

def login(request):
    # ログイン

    # セッション削除
    request.session.flush()

    return render(request, "login/index.html")


def index(request):
    # ログイン後のメニュー

    logger.debug("seqUserId" in request.session)

    if ("seqUserId" in request.session) :
        # ログイン済の場合
        logger.info(request.session["seqUserId"])
        return render(request, "index.html")

    if (request.method == "GET") :
        return render(request, "login/index.html")
    
    
    # USER_DATAを検索し、対象のユーザが登録されているか確認する
    seqUserId = request.POST["seq_user_id"]
    user = UserData.objects.get(seq_user_id = seqUserId)
    logger.debug(user)

    if (user is None):
        params = {
            "errorMessage": "ユーザが存在しません"
        }
        return render(request, "login/index.html", params)

    # セッションにユーザIDを保持
    request.session["seqUserId"] = seqUserId

    return render(request, "index.html")


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


def user_edit(request):
    # ユーザ編集

    sessionSeqUserId = request.session["seqUserId"]
    oldUser = UserData.objects.get(seq_user_id=sessionSeqUserId)
    if (request.method == "POST") :
        user = UserEditForm(request.POST, instance = oldUser)
        user.save()
        return render(request, "user/edit.html")
    
    params = {
        "seqUserId": sessionSeqUserId,
        "form": UserEditForm(instance = oldUser),
    }

    return render(request, "user/edit.html", params)
