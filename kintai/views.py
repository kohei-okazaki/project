import logging
from django.shortcuts import redirect, render
from .forms import UserCreateForm, UserEditForm
from .models import UserData


logger = logging.getLogger(__name__)

# ログイン
def login(request):

    # セッション削除
    request.session.flush()

    return render(request, "login/index.html")

# ログイン後のメニュー
def index(request):

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

    sessionSeqUserId = request.session["seqUserId"]
    currentUser = UserData.objects.get(seq_user_id=sessionSeqUserId)
    if (request.method == "POST") :
        user = UserEditForm(request.POST, instance = currentUser)
        user.save()
        return render(request, "user/edit.html")
    
    params = {
        "form": UserEditForm(instance = currentUser),
    }

    return render(request, "user/edit.html", params)
