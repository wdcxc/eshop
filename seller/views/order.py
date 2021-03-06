from datetime import datetime

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

    @loginRequire()
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

    @loginRequire()
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

    @loginRequire()
    def refund(self, request):
        """退款处理"""
        seller = self.context["seller"]

        if request.method == "GET":
            refunds = OrderProductModel.objects.filter(product__seller=seller,
                                                       status=OrderProductModel.REFUND).order_by('addTime')
            page = request.GET.get("page")
            paginator = Paginator(refunds, 1)
            try:
                self.context["refunds"] = paginator.page(page)
            except EmptyPage:
                self.context["refunds"] = paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                self.context["refunds"] = paginator.page(1)
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            id = request.POST.get("id")
            try:
                ordProduct = OrderProductModel.objects.get(id=id, product__seller=seller)
                status = request.POST.get("status")
                refundDealResult = request.POST.get("refundDealResult")
                ordProduct.status = status
                ordProduct.refundDealResult = refundDealResult
                ordProduct.refundDealTime = datetime.now()
                ordProduct.save()
            except Exception as e:
                self.context = {"code": 4, "msg": "退款处理失败", "data": {"id": id}}
            else:
                self.context = {"code": 200, "msg": "退款处理成功", "data": {"id": id}}
