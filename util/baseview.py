import functools

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .captcha import Captcha


class BaseView(View):
    RESPONSE_TYPE_JSON = "JSON"
    RESPONSE_TYPE_IMAGE = "IMAGE"
    RESPONSE_TYPE_DEFAULT = "DEFAULT"
    RESPONSE_TYPE_REDIRECT = "REDIRECT"

    def __init__(self):
        self.request_ = {}
        self.response_ = {"type": "DEFAULT"}
        self.context = {}

    def beforeAction(self, request):
        request.session.set_expiry(settings.SESSION_EXPIRE_AGE)
        self.request_["appadmin"], self.request_["controller"], self.request_["action"] = request.path.split("/")[1:4]
        self.context["appadmin"], self.context["controller"], self.context["action"] = self.request_["appadmin"], \
                                                                                       self.request_["controller"], \
                                                                                       self.request_["action"]

    def afterAction(self, request):
        if self.response_["type"] == self.RESPONSE_TYPE_JSON:
            return JsonResponse(self.context)
        elif self.response_["type"] == self.RESPONSE_TYPE_IMAGE:
            return HttpResponse(self.context["image"], "image/png")
        elif self.response_["type"] == self.RESPONSE_TYPE_DEFAULT:
            responsePath = "{app}/{controller}/{action}.html".format(app=self.request_["appadmin"],
                                                                     controller=self.request_["controller"],
                                                                     action=self.request_["action"])
            return render(request, responsePath, self.context)
        elif self.response_["type"] == self.RESPONSE_TYPE_REDIRECT:
            return redirect(self.context["redirectPath"])

    def dispatch(self, request, *args, **kwargs):
        """请求处理"""
        self.beforeAction(request)
        getattr(self, self.request_["action"])(request)
        return self.afterAction(request)

    def generateCaptcha(self, request):
        """验证码图像生成"""
        self.response_["type"] = "IMAGE"
        captcha = Captcha().geneCaptchaImage()
        request.session["captchaCode"] = captcha["captchaCode"].lower()
        self.context["image"] = captcha["captchaImageBuff"]

    def valifyCaptcha(self, request):
        """验证码验证"""
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        captchaCode = request.POST.get("captchaCode", "").lower()
        if "captchaCode" in request.session and captchaCode == request.session["captchaCode"]:
            self.context = {"code": 200, "msg": "验证码正确", "data": {"input": captchaCode}}
        else:
            self.context = {"code": 411, "msg": "验证码错误", "data": {"input": captchaCode}}


def loginRequire(redirectUrl=None):
    """登录要求装饰器"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(view, request, *args, **kwargs):
            if "user" not in request.session or request.session["user"] is None or request.session["user"]["app"] != view.request_["appadmin"]:
                if redirectUrl:
                    view.context["redirectPath"] = redirectUrl
                else:
                    view.context["redirectPath"] = "/{app}/{controller}/login".format(app=view.request_["appadmin"],
                                                                                      controller="common")
                view.response_["type"] = BaseView.RESPONSE_TYPE_REDIRECT
            else:
                view.context["user"] = request.session["user"]
                return func(view, request, *args, **kwargs)

        return wrapper

    return decorator


def valifyCaptcha(errcode, errmsg="验证码错误"):
    """验证码验证装饰器"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            view, request = args[0], args[1]
            captchaCode = request.POST.get("captchaCode", "").lower()
            if "captchaCode" in request.session and captchaCode == request.session["captchaCode"]:
                del request.session["captchaCode"]
                func(*args, **kwargs)
            else:
                view.response_["type"] = BaseView.RESPONSE_TYPE_JSON
                view.context = {"code": errcode, "msg": errmsg, "data": {"input": captchaCode}}
                args = (view, args[1:])

        return wrapper

    return decorator
