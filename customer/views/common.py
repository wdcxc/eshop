# coding:utf-8
import hashlib

from models.customer import CustomerModel
from util.baseview import BaseView, valifyCaptcha
from util.regex import Regex


class CommonView(BaseView):
    def index(self, request):
        pass

    def information(self, request):
        pass

    def address(self, request):
        pass

    def order(self, request):
        pass

    def evaluate(self, request):
        pass

    def collection(self, request):
        pass

    def consult(self, request):
        pass

    def opinion(self, request):
        pass

    def message(self, request):
        pass

    def bill(self, request):
        pass

    def refundapply(self, request):
        pass

    def goodsevaluate(self, request):
        pass

    def login(self, request):
        pass

    def register(self, request):
        pass

    def forgetpwd(self, request):
        pass

    @valifyCaptcha(errcode=401)
    def doLogin(self, request):
        """买家登录
        允许用户名/手机/邮箱登录
        """
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        customerKeys = ("account", "password")
        customer = {}
        for key in customerKeys:
            customer[key] = request.POST.get(key)

        # 账号密码验证
        customer["password"] = hashlib.sha512(customer["password"].encode("utf-8")).hexdigest()
        username_num = CustomerModel.objects.filter(name__exact=customer["account"],
                                               password__exact=customer["password"]).count()
        mobile_num = CustomerModel.objects.filter(mobile__exact=customer["account"],
                                             password__exact=customer["password"]).count()
        email_num = CustomerModel.objects.filter(email__exact=customer["account"],
                                            password__exact=customer["password"]).count()
        if username_num + mobile_num + email_num == 3:
            del request.session["captchaCode"]
            self.context = {"code": 200, "msg": "登录成功", "data": {}}
        else:
            self.context = {"code": 410, "msg": "账号或密码错误", "data": {}}

    @valifyCaptcha(errcode=412)
    def doRegister(self, request):
        """买家注册"""
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        customerKeys = ("name", "password", "mobile", "email", "captchaCode")
        customer = {}
        for key in customerKeys:
            customer[key] = request.POST.get(key)

        # 正则验证数据
        regex = Regex()
        if regex.validateUsername(customer["name"]) is False:
            self.context = {"code": 403, "msg": "用户名须为6-30位字母数字字符组成", "data": {}}
        elif regex.validatePassword(customer["password"]) is False:
            self.context = {"codd": 404, "msg": "密码须位8-30位字母数字字符组成", "data": {}}
        elif regex.validateMobile(customer["mobile"]) is False:
            self.context = {"codd": 405, "msg": "手机格式验证错误", "data": {}}
        elif regex.validateEmail(customer["email"]) is False:
            self.context = {"codd": 406, "msg": "邮箱格式验证错误", "data": {}}
        else:
            # 数据库查重
            if CustomerModel.objects.filter(name__exact=customer["username"]).exists():
                self.context = {"code": 407, "msg": "用户名已存在", "data": {}}
            elif CustomerModel.objects.filter(mobile__exact=customer["mobile"]).exists():
                self.context = {"code": 408, "msg": "手机已存在", "data": {}}
            elif CustomerModel.objects.filter(email__exact=customer["email"]).exists():
                resutl = {"code": 409, "msg": "邮箱已存在", "data": {}}
            else:
                # 插入新数据
                customer = CustomerModel(name=customer["username"],
                                    password=hashlib.sha512(customer["password"]).hexdigest(),
                                    mobile=customer["mobile"],
                                    email=customer["email"])
                customer.save()
                del request.session["captchaCode"]
                self.context = {"code": 200, "msg": "注册成功", "data": {}}
