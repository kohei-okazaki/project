import logging
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import LoginForm, UserCreateForm, UserEditForm
from .models import UserData

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
