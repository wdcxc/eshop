# coding:utf-8

from customer.views.customerbaseview import CustomerBaseView
from models.customer import CustomerModel
from models.order import OrderModel
from util.baseview import loginRequire
from util.geodata import GeoData
from util.upload import Upload


class InformationView(CustomerBaseView):
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

    @loginRequire()
    def information(self, request):
        """个人信息"""
        if request.method == "GET":
            self.context['customer'].birthday = self.context["customer"].birthday.strftime("%Y-%m-%d")
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("nickname", "truename", "email", "mobile", "birthday", "avatar", "sex")
            dict = {}
            for key in keys:
                dict[key] = request.POST.get(key)
            CustomerModel.objects.filter(id=request.session["user"]["id"]).update(**dict)
            self.context = {"code": 200, "msg": "修改个人信息成功", "data": {}}

    @loginRequire()
    def uploadAvatar(self, request):
        """上传买家头像"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        avatar = request.FILES["img"]
        self.context = Upload.uploadImg(img=avatar, dir="customer")

    @loginRequire()
    def address(self, request):
        """收货地址管理"""
        customer = self.context["customer"]
        self.context["addresses"] = customer.receiveAddresses.all()
        self.context["provinces"] = GeoData.geoData.keys()

    @loginRequire()
    def addAddress(self,request):
        """新增收货地址"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        keys = ("name","mobile","address","province","dist","city")
        dict = {}
        for key in keys:
            dict[key] = request.POST.get(key)
        self.context["customer"].receiveAddresses.create(**dict)
        self.context = {"code":200,"msg":"新增收获地址成功","data":{}}

    @loginRequire()
    def citys(self,request):
        """获取城市列表"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        print(request.GET)
        provice = request.GET.get("province")
        citys = list(GeoData.geoData[provice].keys())
        self.context = {"code":200,"msg":"获取城市列表成功","data":{"province":provice,"citys":citys}}

    @loginRequire()
    def dists(self, request):
        """获取区列表"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        provice = request.GET.get("province")
        city = request.GET.get("city")
        dists = GeoData.geoData[provice][city]
        self.context = {"code": 200, "msg": "获取城市列表成功", "data": {"province": provice, "city": city,"dists":dists}}