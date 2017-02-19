from django.shortcuts import render
from django.http import JsonResponse
import hashlib


def login(request):
    return render(request,"customer/login.html")


def register(request):
    return render(request,"customer/register.html")


def forgetPwd(request):
    return render(request,"customer/forgetPwd.html")


def doLogin(request):
    # todo
    print(request.POST.get("customer"))
    return JsonResponse({"code":200})