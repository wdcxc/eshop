import hashlib
from datetime import datetime

from django.urls import reverse

from admin.views.adminbaseview import AdminBaseView
from models.admin import AdminModel
from models.customer import CustomerModel
from models.seller import SellerModel
from util.baseview import loginRequire
from util.baseview import valifyCaptcha


class CommonView(AdminBaseView):
    def login(self, request):
        pass

    @valifyCaptcha(errcode=412)
    def doLogin(self, request):
        """登录"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        userKeys = ["username", "password"]
        user = {}
        for key in userKeys:
            user[key] = request.POST.get(key)

        user["password"] = hashlib.sha512(user["password"].encode("utf-8")).hexdigest()
        try:
            loginUser = AdminModel.objects.get(username=user["username"], password=user["password"])
            loginUser.loginTime = datetime.now()
            loginUser.save()
            request.session["user"] = {"id": loginUser.id, "username": loginUser.username,
                                       "loginTime": str(loginUser.loginTime),"app":self.request_["appadmin"]}
            self.context = {"code": 200, "msg": "登陆成功", "data": {"username": loginUser.username}}
        except Exception as e:
            self.context = {"code": 413, "msg": "用户名或密码错误", "data": {}}

    def logout(self, request):
        """退出账号"""
        del request.session["user"]
        self.response_["type"] = self.RESPONSE_TYPE_REDIRECT
        self.context["redirectPath"] = reverse("admin:login")

    @loginRequire()
    def index(self, request):
        """总览"""
        customers = CustomerModel.objects.all().order_by("-registTime")[:5]
        self.context["customers"] = customers
        sellers = SellerModel.objects.all().order_by("-registTime")[:5]
        self.context["sellers"] = sellers

    def forbidden(self,request):
        pass
