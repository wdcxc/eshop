from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from models.order import OrderProductModel
from seller.views.sellerbaseview import SellerBaseView
from util.baseview import loginRequire


class OrderView(SellerBaseView):
    @loginRequire()
    def order(self, request):
        """待发货订单"""
        seller = self.context["seller"]
        ordProducts = OrderProductModel.objects.filter(product__seller=seller,
                                                       status=OrderProductModel.UNSEND).order_by("-addTime")
        page = request.GET.get("page")
        paginator = Paginator(ordProducts, 2)
        try:
            self.context["products"] = paginator.page(page)
        except EmptyPage:
            self.context["products"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["products"] = paginator.page(1)

    def receiveorder(self, request):
        """待收货订单"""
        seller = self.context["seller"]
        ordProducts = OrderProductModel.objects.filter(product__seller=seller,
                                                       status=OrderProductModel.UNRECEIVE).order_by("-addTime")
        page = request.GET.get("page")
        paginator = Paginator(ordProducts, 2)
        try:
            self.context["products"] = paginator.page(page)
        except EmptyPage:
            self.context["products"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["products"] = paginator.page(1)

    def evaluateorder(self, request):
        """待评价订单"""
        seller = self.context["seller"]
        ordProducts = OrderProductModel.objects.filter(product__seller=seller,
                                                       status=OrderProductModel.UNEVALUATE).order_by("-addTime")
        page = request.GET.get("page")
        paginator = Paginator(ordProducts, 2)
        try:
            self.context["products"] = paginator.page(page)
        except EmptyPage:
            self.context["products"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["products"] = paginator.page(1)

    @loginRequire()
    def sendProduct(self, request):
        """发货"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        ordPd = OrderProductModel.objects.get(id=id)
        if ordPd.status == OrderProductModel.UNSEND:
            ordPd.status = OrderProductModel.UNRECEIVE
            ordPd.save()
            self.context = {"code": 200, "msg": "商品已发货", "data": {"id": id}}
        else:
            self.context = {"code": 4, "msg": "商品状态出错", "data": {"id": id}}
