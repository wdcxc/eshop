# coding:utf-8
import hashlib

from django.urls import reverse

from customer.views.customerbaseview import CustomerBaseView
from models.customer import CustomerModel
from util.baseview import BaseView, valifyCaptcha
from util.regex import Regex


class CommonView(CustomerBaseView):
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

    def forgetpwd(self, request):
        pass

    def login(self, request):
        refer = request.META["HTTP_REFERER"]
        refer_app = refer.split("/")[3]
        if refer_app != self.request_["appadmin"]:
            request.session["refer_app"] = refer_app
        request.session["refer"] = refer

    @valifyCaptcha(errcode=401)
    def doLogin(self, request):
        """买家登录
        允许用户名/手机/邮箱登录
        """
        self.response_["type"] = self.RESPONSE_TYPE_JSON

        customerKeys = ("account", "password")
        customer = {}
        for key in customerKeys:
            customer[key] = request.POST.get(key)

        # 账号密码验证
        customer["password"] = hashlib.sha512(customer["password"].encode("utf-8")).hexdigest()
        username_num = CustomerModel.objects.filter(name=customer["account"],
                                                    password=customer["password"]).count()
        mobile_num = CustomerModel.objects.filter(mobile=customer["account"],
                                                  password=customer["password"]).count()
        email_num = CustomerModel.objects.filter(email=customer["account"],
                                                 password=customer["password"]).count()
        if username_num + mobile_num + email_num == 1:
            if username_num:
                loginedCustomer = CustomerModel.objects.get(name=customer["account"])
            elif mobile_num:
                loginedCustomer = CustomerModel.objects.get(mobile=customer["account"])
            elif email_num:
                loginedCustomer = CustomerModel.objects.get(email=customer["account"])
            request.session["user"] = {"id": loginedCustomer.id, "app": self.request_["appadmin"]}
            if "refer" in request.session:
                self.context = {"code": 200, "msg": "登录成功", "data": {"account": loginedCustomer.id,"redirectPath":request.session["refer"]}}
            else:
                self.context = {"code": 200, "msg": "登录成功", "data": {"account": loginedCustomer.id,"redirectPath":reverse("customer:index")}}
        else:
            self.context = {"code": 410, "msg": "账号或密码错误", "data": {}}

    def register(self, request):
        pass

    @valifyCaptcha(errcode=412)
    def doRegister(self, request):
        """买家注册"""
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        customerKeys = ("name", "password", "mobile", "email")
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
            if CustomerModel.objects.filter(name=customer["name"]).exists():
                self.context = {"code": 407, "msg": "用户名已存在", "data": {}}
            elif CustomerModel.objects.filter(mobile=customer["mobile"]).exists():
                self.context = {"code": 408, "msg": "手机已存在", "data": {}}
            elif CustomerModel.objects.filter(email=customer["email"]).exists():
                self.context = {"code": 409, "msg": "邮箱已存在", "data": {}}
            else:
                # 插入新数据
                customer = CustomerModel(name=customer["name"],
                                         password=hashlib.sha512(customer["password"].encode("utf-8")).hexdigest(),
                                         mobile=customer["mobile"],
                                         email=customer["email"])
                customer.save()
                self.context = {"code": 200, "msg": "注册成功", "data": {"id": customer.id}}

    def logout(self,request):
        """退出登陆"""
        self.response_["type"]=self.RESPONSE_TYPE_REDIRECT
        if "user" in request.session:
            del request.session["user"]
        if "customer" in self.context:
            del self.context["customer"]
        self.context["redirectPath"] = reverse("customer:login")