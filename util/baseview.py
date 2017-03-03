import functools

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
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

    def dispatch(self, request, *args, **kwargs):
        """请求处理"""
        self.request_["app"], self.request_["action"] = request.path.split("/")[1:3]
        self.context["activeAction"] = self.request_["action"]
        getattr(self, self.request_["action"])(request)
        if self.response_["type"] == self.RESPONSE_TYPE_JSON:
            return JsonResponse(self.context)
        elif self.response_["type"] == self.RESPONSE_TYPE_IMAGE:
            return HttpResponse(self.context["image"], "image/png")
        elif self.response_["type"] == self.RESPONSE_TYPE_DEFAULT:
            responsePath = "{app}/{action}.html".format(app=self.request_["app"], action=self.request_["action"])
            return render(request, responsePath, self.context)
        elif self.response_["type"] == self.RESPONSE_TYPE_REDIRECT:
            redirectPath = "{app}:{action}".format(app=self.request_["app"],action=self.request_["action"])
            return redirect(redirectPath)

    def getCaptchaImage(self, request):
        """验证码图像生成"""
        self.response_["type"] = "IMAGE"
        captcha = Captcha().geneCaptchaImage()
        request.session["captchaCode"] = captcha["captchaCode"]
        self.context["image"] = captcha["captchaImageBuff"]

    def valifyCaptcha(self, request):
        """验证码验证"""
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        captchaCode = request.POST.get("captchaCode").lower()
        if captchaCode == request.session["captchaCode"]:
            self.context = {"code": 200, "msg": "验证码正确", "data": {"input": captchaCode}}
        else:
            self.context = {"code": 411, "msg": "验证码错误", "data": {"input": captchaCode}}


def loginRequire(loginUrl=None):
    """登录要求装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            view, request = args[0], args[1]
            if "user" not in request.session or request.session["user"] is None:
                view.request_["action"] = "login"
                view.response_["type"] = BaseView.RESPONSE_TYPE_REDIRECT
                args = (view,args[1:])
            return func(*args, *kwargs)
        return wrapper
    return decorator
