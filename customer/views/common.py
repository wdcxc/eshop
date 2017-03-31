# coding:utf-8
import hashlib

from customer.views.customerbaseview import CustomerBaseView
from models.customer import CustomerModel
from models.order import OrderModel
from util.baseview import BaseView, valifyCaptcha, loginRequire
from util.regex import Regex
from util.upload import Upload


class CommonView(CustomerBaseView):
    @loginRequire()
    def index(self, request):
        """买家首页"""
        customer = self.context["customer"]
        # 订单
        orders = customer.orders.all().order_by("-addTime")
        self.context["unpayOrderNum"] = orders.filter(status=OrderModel.UNPAY).count()
        self.context["unsendOrderNum"] = orders.filter(status=OrderModel.UNSEND).count()
        self.context["unreceiveOrderNum"] = orders.filter(status=OrderModel.UNRECEIVE).count()
        self.context["unevaluateOrderNum"] = orders.filter(status=OrderModel.UNEVALUATE).count()
        orders = orders[:2]
        for order in orders:
            products = order.products.all()
            order.__dict__.update({"products": products, "totalPrice": 0, "productsNum": products.count()})
            for product in products:
                order.__dict__["totalPrice"] += product.sellPrice
            orderStatusDict = {OrderModel.UNPAY: "待付款", OrderModel.UNSEND: "待发货", OrderModel.UNRECEIVE: "待收获",
                               OrderModel.UNEVALUATE: "待评价"}
            order.__dict__.update({"status": {"code": order.status, "text": orderStatusDict[order.status]}})
        self.context["orders"] = [order.__dict__ for order in orders]
        # 收藏
        collections = customer.collections.all()[:5]
        for collection in collections:
            collection.__dict__.update({"product": collection.product})
        self.context["collections"] = [collection.__dict__ for collection in collections]

    def information(self, request):
        """个人信息"""
        if request.method == "GET":
            self.context['customer'].birthday = self.context["customer"].birthday.strftime("%Y-%m-%d")
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("nickname","truename","email","mobile","birthday","avatar","sex")
            dict = {}
            for key in keys:
                dict[key] = request.POST.get(key)
            CustomerModel.objects.filter(id=request.session["user"]["id"]).update(**dict)
            self.context = {"code":200,"msg":"修改个人信息成功","data":{}}

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
            request.session["user"] = {"id": loginedCustomer.id}
            self.context = {"code": 200, "msg": "登录成功", "data": {"account": loginedCustomer.id}}
        else:
            self.context = {"code": 410, "msg": "账号或密码错误", "data": {}}
        print(self.context)

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

    @loginRequire()
    def uploadAvatar(self,request):
        """上传买家头像"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        avatar = request.FILES["img"]
        self.context = Upload.uploadImg(img=avatar,dir="customer")
