# coding:utf-8
import hashlib

from util.baseview import BaseView
from util.regex import Regex
from .models import Customer


class CustomerView(BaseView):
    def login(self, request):
        pass

    def register(self, request):
        pass

    def forgetPwd(self, request):
        pass

    def doLogin(self, request):
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        customerKeys = ("account", "password", "captchaCode")
        customer = {}
        for key in customerKeys:
            customer[key] = request.POST.get(key)

        # 验证码验证
        if customer["captchaCode"].lower() != request.session["captchaCode"]:
            self.context = {"code": "401", "msg": "验证码验证错误", "data": {}}
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
                self.context = {"code": 200, "msg": "登录成功", "data": {}}
            else:
                self.context = {"code": 410, "msg": "账号或密码错误", "data": {}}

    def doRegister(self, request):
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        customerKeys = ("username", "password", "mobile", "email", "captchaCode")
        customer = {}
        for key in customerKeys:
            customer[key] = request.POST.get(key)

        # 验证验证码
        if customer["captchaCode"].lower() != request.session["captchaCode"]:
            self.context = {"code": 412, "msg": "验证码错误", "data": {"captchaCode": customer["captchaCode"]}}
        else:
            # 正则验证数据
            regex = Regex()
            if regex.validateUsername(customer["username"]) is None:
                self.context = {"code": 403, "msg": "用户名须为6-30位字母数字字符组成", "data": {}}
            elif regex.validatePassword(customer["password"]) is None:
                self.context = {"codd": 404, "msg": "密码须位8-30位字母数字字符组成", "data": {}}
            elif regex.validateMobile(customer["mobile"]) is None:
                self.context = {"codd": 405, "msg": "手机格式验证错误", "data": {}}
            elif regex.validateEmail(customer["email"]) is None:
                self.context = {"codd": 406, "msg": "邮箱格式验证错误", "data": {}}
            else:
                # 数据库查重
                if Customer.objects.filter(username__exact=customer["username"]).exists():
                    self.context = {"code": 407, "msg": "用户名已存在", "data": {}}
                elif Customer.objects.filter(mobile__exact=customer["mobile"]).exists():
                    self.context = {"code": 408, "msg": "手机已存在", "data": {}}
                elif Customer.objects.filter(email__exact=customer["email"]).exists():
                    resutl = {"code": 409, "msg": "邮箱已存在", "data": {}}
                else:
                    # 插入新数据
                    customer = Customer(username=customer["username"],
                                        password=hashlib.sha512(customer["password"]).hexdigest(),
                                        mobile=customer["mobile"],
                                        email=customer["email"])
                    customer.save()
                    del request.session["captchaCode"]
                    self.context = {"code": 200, "msg": "注册成功", "data": {}}


