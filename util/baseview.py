from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .captcha import Captcha


class BaseView(View):
    RESPONSE_TYPE_JSON = "JSON"
    RESPONSE_TYPE_IMAGE = "IMAGE"
    RESPONSE_TYPE_DEFAULT = "DEFAULT"

    def __init__(self):
        self.request_ = {}
        self.response_ = {"type": "DEFAULT"}
        self.context = {}

    def dispatch(self, request, *args, **kwargs):
        self.request_["app"], self.request_["action"] = request.path.split("/")[1:3]
        self.context["activeAction"] = self.request_["action"]
        getattr(self, self.request_["action"])(request)
        if self.response_["type"] == BaseView.RESPONSE_TYPE_JSON:
            return JsonResponse(self.context)
        elif self.response_["type"] == BaseView.RESPONSE_TYPE_IMAGE:
            return HttpResponse(self.context["image"], "image/png")
        elif self.response_["type"] == BaseView.RESPONSE_TYPE_DEFAULT:
            responsePath = "{app}/{action}.html".format(app=self.request_["app"], action=self.request_["action"])
            return render(request, responsePath, self.context)

    def getCaptchaImage(self, request):
        self.response_["type"] = "IMAGE"
        captcha = Captcha().geneCaptchaImage()
        request.session["captchaCode"] = captcha["captchaCode"]
        self.context["image"] = captcha["captchaImageBuff"]

    def valifyCaptcha(self, request):
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        captchaCode = request.POST.get("captchaCode").lower()
        if captchaCode == request.session["captchaCode"]:
            self.context = {"code": 200, "msg": "验证码正确", "data": {"input": captchaCode}}
        else:
            self.context = {"code": 411, "msg": "验证码错误", "data": {"input": captchaCode}}
