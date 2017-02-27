# coding:utf-8
import hashlib

from django.http import JsonResponse,HttpResponse
from django.shortcuts import render

from util.captcha import Captcha
from util.regex import Regex
from .models import Customer


def login(request):
    return render(request, "customer/login.html")


def register(request):
    return render(request, "customer/register.html")


def forgetPwd(request):
    return render(request, "customer/forgetPwd.html")


def doLogin(request):
    customerKeys = ("account", "password", "captchaCode")
    customer = {}
    result = {}
    for key in customerKeys:
        customer[key] = request.POST.get(key)

    # 验证码验证
    if customer["captchaCode"].lower() != request.session["captchaCode"]:
        result = {"code": "401", "msg": "验证码验证错误", "data": {}}
    else:
        # 账号密码验证
        customer["password"] = hashlib.sha512(customer["password"].encode("utf-8")).hexdigest()
        username_num = Customer.objects.filter(username__exact=customer["account"],
                                               password__exact=customer["password"]).count()
        mobile_num = Customer.objects.filter(mobile__exact=customer["account"],
                                             password__exact=customer["password"]).count()
        email_num = Customer.objects.filter(email__exact=customer["account"],
                                            password__exact=customer["password"]).count()
        if username_num + mobile_num + email_num == 3:
            del request.session["captchaCode"]
            result = {"code": 200, "msg": "登录成功", "data": {}}
        else:
            result = {"code": 410, "msg": "账号或密码错误", "data": {}}

    return JsonResponse(result)


def doRegister(request):
    customerKeys = ("username", "password", "mobile", "email","captchaCode")
    customer = {}
    result = {}
    for key in customerKeys:
        customer[key] = request.POST.get(key)

    # 验证验证码
    if customer["captchaCode"].lower() != request.session["captchaCode"]:
        return JsonResponse({"code":412,"msg":"验证码错误","data":{"captchaCode":customer["captchaCode"]}})

    # 正则验证数据
    regex = Regex()
    if regex.validateUsername(customer["username"]) is None:
        result = {"code": 403, "msg": "用户名须为6-30位字母数字字符组成", "data": {}}
    elif regex.validatePassword(customer["password"]) is None:
        result = {"codd": 404, "msg": "密码须位8-30位字母数字字符组成", "data": {}}
    elif regex.validateMobile(customer["mobile"]) is None:
        result = {"codd": 405, "msg": "手机格式验证错误", "data": {}}
    elif regex.validateEmail(customer["email"]) is None:
        result = {"codd": 406, "msg": "邮箱格式验证错误", "data": {}}
    else:
        # 数据库查重
        if Customer.objects.filter(username__exact=customer["username"]).exists():
            result = {"code": 407, "msg": "用户名已存在", "data": {}}
        elif Customer.objects.filter(mobile__exact=customer["mobile"]).exists():
            result = {"code": 408, "msg": "手机已存在", "data": {}}
        elif Customer.objects.filter(email__exact=customer["email"]).exists():
            resutl = {"code": 409, "msg": "邮箱已存在", "data": {}}
        else:
            # 插入新数据
            customer = Customer(username=customer["username"],
                                password=hashlib.sha512(customer["password"]).hexdigest(), mobile=customer["mobile"],
                                email=customer["email"])
            customer.save()
            del request.session["captchaCode"]
            result = {"code": 200, "msg": "注册成功", "data": {}}

    return JsonResponse(result)


def captcha(request):
    # captcha = Captcha().geneCaptcha("customer", action)
    captcha = Captcha().geneCaptchaImage()
    request.session["captchaCode"] = captcha["captchaCode"]
    return HttpResponse(captcha["captchaImageBuff"],"image/png")

def valifyCaptcha(request):
    captchaCode = request.POST.get("captchaCode").lower()
    if captchaCode == request.session["captchaCode"]:
        return JsonResponse({"code":200,"msg":"验证码正确","data":{"input":captchaCode}})
    else:
        return JsonResponse({"code":411,"msg":"验证码错误","data":{"input":captchaCode}})
