# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
import hashlib
from django.core.signing import TimestampSigner
from .models import Customer
import re
from util.captcha import Captcha
from util.regex import Regex


def login(request):
    return render(request, "customer/login.html")


def register(request):
    return render(request, "customer/register.html")


def forgetPwd(request):
    return render(request, "customer/forgetPwd.html")


def doLogin(request):
    customerKeys = ("account", "password", "captcha")
    customer = {}
    result = {}
    for key in customerKeys:
        customer[key] = request.POST.get(key)

    # 验证码验证
    if not Captcha().validate("customer", "login", customer["captcha"]):
        result = {"code": "401", "msg": "验证码验证错误", "data": {}}
    else:
        # 账号密码验证
        customer["password"] = hashlib.sha512(customer["password"]).hexdigest()
        try:
            username_num = Customer.objects.filter(username__exact=customer["account"],
                                                   password__exact=customer["password"]).count()
            mobile_num = Customer.objects.filter(mobile__exact=customer["account"],
                                                 password__exact=customer["password"]).count()
            email_num = Customer.objects.filter(email__exact=customer["account"],
                                                password__exact=customer["password"]).count()
            if username_num + mobile_num + email_num == 3:
                result = {"code": 200, "msg": "登录成功", "data": {}}
            else:
                result = {"code": 410, "msg": "账号或密码错误", "data": {}}
        except Customer.DoesNotExist:
            result = {"code": 402, "msg": "账号或密码错误", "data": {}}

    return JsonResponse(result)


def doRegister(request):
    customerKeys = ("username", "password", "mobile", "email")
    customer = {}
    result = {}
    for key in customerKeys:
        customer[key] = request.POST.get(key)

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
            result = {"code": 200, "msg": "注册成功", "data": {}}

    return JsonResponse(result)


def captcha(request, action):
    # captcha = Captcha().geneCaptcha("customer", action)
    captcha = Captcha().geneCaptchaImage()
    return JsonResponse(
        {"code": 200, "msg": "generate customer {action} validate code success".format(action=action),
         "data": {"captchaImagePath": captcha["captchaImagePath"]}})
