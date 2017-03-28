import hashlib

from models.seller import Seller
from util.baseview import BaseView,valifyCaptcha
from util.regex import Regex


class CommonView(BaseView):
    def index(self, request):
        pass

    def login(self, request):
        pass

    def register(self, request):
        pass

    def forgetpwd(self, request):
        pass

    def consult(self, request):
        pass

    def opinion(self, request):
        pass

    def verify(self, request):
        pass

    def personalinfo(self, request):
        pass

    def shopinfo(self, request):
        pass

    @valifyCaptcha(errcode=401)
    def doLogin(self, request):
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        sellerKeys = ("account", "password")
        seller = {}
        for key in sellerKeys:
            seller[key] = request.POST.get(key)

        # 账号密码验证
        seller["password"] = hashlib.sha512(seller["password"].encode("utf-8")).hexdigest()
        username_num = Seller.objects.filter(username__exact=seller["account"],
                                               password__exact=seller["password"]).count()
        mobile_num = Seller.objects.filter(mobile__exact=seller["account"],
                                             password__exact=seller["password"]).count()
        email_num = Seller.objects.filter(email__exact=seller["account"],
                                            password__exact=seller["password"]).count()
        if username_num + mobile_num + email_num == 3:
            del request.session["captchaCode"]
            self.context = {"code": 200, "msg": "登录成功", "data": {}}
        else:
            self.context = {"code": 410, "msg": "账号或密码错误", "data": {}}

    @valifyCaptcha(errcode=412)
    def doRegister(self, request):
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        sellerKeys = ("username", "password", "mobile", "email", "captchaCode")
        seller = {}
        for key in sellerKeys:
            seller[key] = request.POST.get(key)

        # 正则验证数据
        regex = Regex()
        if regex.validateUsername(seller["username"]) is None:
            self.context = {"code": 403, "msg": "用户名须为6-30位字母数字字符组成", "data": {}}
        elif regex.validatePassword(seller["password"]) is None:
            self.context = {"codd": 404, "msg": "密码须位8-30位字母数字字符组成", "data": {}}
        elif regex.validateMobile(seller["mobile"]) is None:
            self.context = {"codd": 405, "msg": "手机格式验证错误", "data": {}}
        elif regex.validateEmail(seller["email"]) is None:
            self.context = {"codd": 406, "msg": "邮箱格式验证错误", "data": {}}
        else:
            # 数据库查重
            if Seller.objects.filter(username__exact=seller["username"]).exists():
                self.context = {"code": 407, "msg": "用户名已存在", "data": {}}
            elif Seller.objects.filter(mobile__exact=seller["mobile"]).exists():
                self.context = {"code": 408, "msg": "手机已存在", "data": {}}
            elif Seller.objects.filter(email__exact=seller["email"]).exists():
                resutl = {"code": 409, "msg": "邮箱已存在", "data": {}}
            else:
                # 插入新数据
                seller = Seller(username=seller["username"],
                                    password=hashlib.sha512(seller["password"]).hexdigest(),
                                    mobile=seller["mobile"],
                                    email=seller["email"])
                seller.save()
                del request.session["captchaCode"]
                self.context = {"code": 200, "msg": "注册成功", "data": {}}
