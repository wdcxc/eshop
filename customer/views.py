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
    customerKeys = ("username","password","valicode")
    customer = {}
    for key in customerKeys:
        customer[key] = request.POST.get(key)
    # 验证码验证 todo
    # 验证账号密码 todo
    customer["password"] = hashlib.sha512(customer["password"]).hexdigest()
    return JsonResponse({"code":200})