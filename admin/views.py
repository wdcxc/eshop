from django.http import HttpResponse
from django.shortcuts import render

from util.captcha import Captcha


def login(request):
    return render(request,"admin/login.html",{"hi":"admin"})

def index(request):
    return render(request,"admin/index.html")

def getCaptchaImage(request):
    captcha = Captcha().geneCaptchaImage()
    request.session["captchaCode"] = captcha["captchaCode"]
    return HttpResponse(captcha["captchaImageBuff"],"image/png")

