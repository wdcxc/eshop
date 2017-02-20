# encoding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
import hashlib
from django.core.signing import TimestampSigner
from .models import Customer


def login(request):
    return render(request, "customer/login.html")


def register(request):
    return render(request, "customer/register.html")


def forgetPwd(request):
    return render(request, "customer/forgetPwd.html")


def doLogin(request):
    customerKeys = ("username", "password", "valicode")
    customer = {}
    valipass = False
    result = {}
    for key in customerKeys:
        customer[key] = request.POST.get(key)

    # 验证码验证
    timeSigner = TimestampSigner()
    try:
        valicode = timeSigner.unsign("customer-login" + customerKeys["valicode"], max_age=300)
        if valicode == "customer-login":
            valipass = True
    except Exception:
        result = {"code": "400", "msg": "验证码验证错误", "data": {}}

    # 验证账号密码
    if not valipass:
        result = {"code": "401", "msg": "验证码验证错误", "data": {}}
    else:
        customer["password"] = hashlib.sha512(customer["password"]).hexdigest()
        try:
            customer = Customer.objects.get(username__exact=customer["username"], password__exact=customer["password"])
            result = {"code": 200, "msg": "登录成功", "data": {}}
        except Customer.DoesNotExist:
            result = {"code": 402, "msg": "账号或密码错误", "data": {}}

    return JsonResponse(result)


def valicode(request):
    timeSigner = TimestampSigner()
    valicode = timeSigner.sign("customer-login")
    return JsonResponse(
        {"code": 200, "msg": "generate customer login validate code success",
         "data": {"valicode": valicode[valicode.index(":"):]}})
