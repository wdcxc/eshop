from datetime import datetime

from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from customer.views.customerbaseview import CustomerBaseView
from models.order import OrderProductModel
from util.baseview import loginRequire


class OrderView(CustomerBaseView):
    @loginRequire()
    def receiveorder(self, request):
        """未收货订单"""
        customer = self.context["customer"]
        unsendProducts = OrderProductModel.objects.filter(order__in=customer.orders.all(),
                                                          status=OrderProductModel.UNRECEIVE).order_by("-addTime")
        paginator = Paginator(unsendProducts, 2)
        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        self.context["products"] = products

    @loginRequire()
    def evaluateorder(self, request):
        """未评价订单"""
        customer = self.context["customer"]
        unsendProducts = OrderProductModel.objects.filter(order__in=customer.orders.all(),
                                                          status=OrderProductModel.UNEVALUATE).order_by("-addTime")
        paginator = Paginator(unsendProducts, 2)
        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        self.context["products"] = products

    @loginRequire()
    def order(self, request):
        """未发货订单"""
        customer = self.context["customer"]
        unsendProducts = OrderProductModel.objects.filter(order__in=customer.orders.all(),
                                                          status=OrderProductModel.UNSEND).order_by("-addTime")
        paginator = Paginator(unsendProducts, 2)
        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        self.context["products"] = products

    @loginRequire()
    def refund(self, request):
        """订单退款"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        refundReason = request.GET.get("refundReason")
        customer = self.context["customer"]
        try:
            ordProduct = OrderProductModel.objects.get(id=id, order__customer=customer)
            ordProduct.status = OrderProductModel.REFUND
            ordProduct.refundReason = refundReason
            ordProduct.refundTime = datetime.now()
            ordProduct.save()
        except Exception as e:
            self.context = {"code": 4, "msg": "退款失败", "data": {"id": id}}
        else:
            self.context = {"code": 200, "msg": "退款成功", "data": {"id": id}}

    @loginRequire()
    def receiveProduct(self, request):
        """收货"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        customer = self.context["customer"]
        try:
            ordProduct = OrderProductModel.objects.get(id=id, order__customer=customer)
            ordProduct.status = OrderProductModel.UNEVALUATE
            ordProduct.receiveTime = datetime.now()
            ordProduct.save()
        except Exception as e:
            self.context = {"code": 4, "msg": "收货失败", "data": {"id": id}}
        else:
            self.context = {"code": 200, "msg": "收货成功", "data": {"id": id}}

    @loginRequire()
    def goodsevaluate(self,request):
        if request.method == "GET":
            id = request.GET.get("id")
            customer = self.context["customer"]
            ordProduct = OrderProductModel.objects.get(id=id,order__customer=customer)
            self.context["product"] = ordProduct
        elif request.method == "POST":
            pass