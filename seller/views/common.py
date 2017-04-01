import hashlib

from django.conf import settings

from models.seller import SellerModel
from util.baseview import BaseView, valifyCaptcha, loginRequire
from util.regex import Regex
from util.upload import Upload


class CommonView(BaseView):
    @loginRequire()
    def index(self, request):
        seller = SellerModel.objects.get(id=request.session["user"]["id"])
        orderProducts = seller.orderProducts.all().order_by("-addTime")[:2]
        self.context["seller"] = seller
        self.context["orderProducts"] = orderProducts

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
        """买家信息"""
        if request.method == "GET":
            seller = SellerModel.objects.get(id=request.session["user"]["id"])
            self.context["seller"] = seller
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("truename", "shopName", "shopAddress", "idno", "email", "mobile", "thumbnail")
            dict = {}
            for key in keys:
                dict[key] = request.POST.get(key)
            SellerModel.objects.filter(id=request.session["user"]["id"]).update(**dict)
            self.context = {"code": 200, "msg": "修改卖家信息成功", "data": {}}

    def order(self, request):
        pass

    def goodslist(self, request):
        pass
        # todo

    def addgoods(self, request):
        pass
        # todo

    @valifyCaptcha(errcode=401)
    def doLogin(self, request):
        """商家登录"""
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        sellerKeys = ("account", "password")
        seller = {}
        for key in sellerKeys:
            seller[key] = request.POST.get(key)

        # 账号密码验证
        seller["password"] = hashlib.sha512(seller["password"].encode("utf8")).hexdigest()
        username_num = SellerModel.objects.filter(name=seller["account"],
                                                  password=seller["password"]).count()
        mobile_num = SellerModel.objects.filter(mobile=seller["account"],
                                                password=seller["password"]).count()
        email_num = SellerModel.objects.filter(email=seller["account"],
                                               password=seller["password"]).count()
        if username_num + mobile_num + email_num == 1:
            if username_num:
                seller = SellerModel.objects.get(name=seller["account"])
            elif mobile_num:
                seller = SellerModel.objects.get(mobile=seller["account"])
            elif email_num:
                seller = SellerModel.objects.get(email=seller["account"])
            request.session["user"] = {"id": seller.id, "app": self.request_["appadmin"]}
            self.context = {"code": 200, "msg": "登录成功", "data": {}}
        else:
            self.context = {"code": 410, "msg": "账号或密码错误", "data": {}}

    @valifyCaptcha(errcode=412)
    def doRegister(self, request):
        """商家注册"""
        self.response_["type"] = BaseView.RESPONSE_TYPE_JSON
        sellerKeys = ("name", "password", "mobile", "email", "idno")
        seller = {}
        for key in sellerKeys:
            seller[key] = request.POST.get(key)

        # 正则验证数据
        regex = Regex()
        if regex.validateUsername(seller["name"]) is False:
            self.context = {"code": 403, "msg": "用户名须为6-30位字母数字字符组成", "data": {}}
        elif regex.validatePassword(seller["password"]) is False:
            self.context = {"code": 404, "msg": "密码须位8-30位字母数字字符组成", "data": {}}
        elif regex.validateMobile(seller["mobile"]) is False:
            self.context = {"code": 405, "msg": "手机格式验证错误", "data": {}}
        elif regex.validateEmail(seller["email"]) is False:
            self.context = {"code": 406, "msg": "邮箱格式验证错误", "data": {}}
        elif regex.validateIdno(seller["idno"]) is False:
            self.context = {"code": 4, "msg": "身份证号码验证错误", "data": {}}
        else:
            seller["password"] = hashlib.sha512(seller["password"].encode("utf8")).hexdigest()
            # 数据库查重
            if SellerModel.objects.filter(name=seller["name"]).exists():
                self.context = {"code": 407, "msg": "用户名已存在", "data": {}}
            elif SellerModel.objects.filter(mobile=seller["mobile"]).exists():
                self.context = {"code": 408, "msg": "手机已存在", "data": {}}
            elif SellerModel.objects.filter(email=seller["email"]).exists():
                self.context = {"code": 409, "msg": "邮箱已存在", "data": {}}
            elif SellerModel.objects.filter(idno=seller["idno"]).exists():
                self.context = {"code": 4, "msg": "身份证号码已存在", "data": {}}
            else:
                # 插入新数据
                seller = SellerModel(**seller)
                seller.save()
                self.context = {"code": 200, "msg": "注册成功", "data": {}}

    @loginRequire()
    def uploadThumbnail(self, request):
        """上传卖家头像"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        img = request.FILES["img"]
        result = Upload.uploadImg(img, "seller")
        if result["code"] == 200:
            seller = SellerModel.objects.get(id=request.session["user"]["id"])
            seller.thumbnail = settings.MEDIA_ROOT + result["data"]["imgUrl"]
            seller.save()
        self.context = result
