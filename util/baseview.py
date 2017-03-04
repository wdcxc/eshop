import functools

from django.conf import settings
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
        request.session.set_expiry(settings.SESSION_EXPIRE_AGE)
        self.request_["app"], self.request_["controller"],self.request_["action"] = request.path.split("/")[1:4]
        self.context["app"],self.context["controller"],self.context["action"] = self.request_["app"],self.request_["controller"],self.request_["action"]

        getattr(self, self.request_["action"])(request)

        if self.response_["type"] == self.RESPONSE_TYPE_JSON:
            return JsonResponse(self.context)
        elif self.response_["type"] == self.RESPONSE_TYPE_IMAGE:
            return HttpResponse(self.context["image"], "image/png")
        elif self.response_["type"] == self.RESPONSE_TYPE_DEFAULT:
            responsePath = "{app}/{controller}/{action}.html".format(app=self.request_["app"], controller=self.request_["controller"],action=self.request_["action"])
            return render(request, responsePath, self.context)
        elif self.response_["type"] == self.RESPONSE_TYPE_REDIRECT:
            return redirect(self.context["redirectPath"])

    def generateCaptcha(self, request):
        """验证码图像生成"""
        self.response_["type"] = "IMAGE"
        captcha = Captcha().geneCaptchaImage()
        request.session["captchaCode"] = captcha["captchaCode"]
        self.context["image"] = captcha["captchaImageBuff"]

    def valifyCaptcha(self, request):
        """验证码验证"""
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        captchaCode = request.POST.get("captchaCode","").lower()
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
                view.context["redirectPath"] = "/{app}/{controller}/login".format(app=view.request_["app"],controller=view.request_["controller"])
                view.response_["type"] = BaseView.RESPONSE_TYPE_REDIRECT
                args = (view,args[1:])
            else:
                return func(*args, *kwargs)
        return wrapper
    return decorator

def valifyCaptcha(errcode,errmsg="验证码错误"):
    """验证码验证装饰器"""
    def decorator(func):
       def wrapper(*args,**kwargs):
           view,request = args[0],args[1]
           captchaCode = request.POST.get("captchaCode","").lower()
           if "captchaCode" in request.session and captchaCode == request.session["captchaCode"]:
               del request.session["captchaCode"]
               func(*args,**kwargs)
           else:
               view.response_["type"] = BaseView.RESPONSE_TYPE_JSON
               view.context = {"code":errcode,"msg":errmsg,"data":{"input":captchaCode}}
               args = (view,args[1:])
       return wrapper
    return decorator
