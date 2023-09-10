from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, "login/index.html")


def index(request):

    params = {
        "seq_user_id": request.POST["seq_user_id"],
        "password": request.POST["password"],
    }
    return render(request, "index.html", params)
