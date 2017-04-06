from datetime import datetime

from app.views.appbaseview import AppBaseView
from models.customer import ShopcartModel
from models.order import OrderModel
from util.baseview import loginRequire


class OrderView(AppBaseView):
    @loginRequire(redirectUrl='/customer/common/login')
    def addOrder(self, request):
        """添加订单"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON

        customer = self.context["customer"]
        newOrder = OrderModel(customer=customer)
        newOrder.save()

        orderStr = request.POST.get("order")[:-1].split(',')
        for order in orderStr:
            scid, num = order.split(":")
            print(scid, num)
            product = ShopcartModel.objects.get(id=scid).product
            newOrder.products.create(product=product, amount=num)

        self.context = {"code": 200, "msg": "添加订单成功", "data": {"id": newOrder.id}}

    @loginRequire(redirectUrl='/customer/common/login')
    def order(self, request):
        """订单详情页"""
        if request.method == "GET":
            customer = self.context["customer"]
            self.context["addresses"] = customer.receiveAddresses.all()
            orderId = request.GET.get("id")
            order = customer.orders.get(id=orderId)
            self.context["products"] = order.products.all()

    @loginRequire(redirectUrl='/customer/common/login')
    def fail(self, request):
        """订单取消成功"""
        id = request.GET.get("id")
        order = self.context["customer"].orders.get(id=id)
        self.context["order"] = order

    @loginRequire(redirectUrl='/customer/common/login')
    def success(self, request):
        """订单支付成功"""
        id = request.GET.get("id")
        order = self.context["customer"].orders.get(id=id)
        self.context["order"] = order

    @loginRequire(redirectUrl='/customer/common/login')
    def payOrder(self, request):
        """支付订单"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON

        customer = self.context["customer"]

        id = request.GET.get("id")
        customerMsg = request.GET.get("customerMsg")
        addressId = request.GET.get("addressId")
        order = customer.orders.get(id=id)

        if order.status not in (OrderModel.UNPAY,OrderModel.CANCEL):
            self.context = {"code": 4, "msg": "订单状态异常", "data": {"id": id}}
        else:
            order.totalPrice = 0
            for ordProduct in order.products.all():
                # 校验订单
                if ordProduct.amount < 0:
                    self.context = {"code": 4, "msg": "商品购买数量不能为负", "data": {"id": id}}
                    break
                elif ordProduct.product.amount < ordProduct.amount:
                    self.context = {"code": 4, "msg": ordProduct.product.name + "商品库存不足,只剩" + ordProduct.product.amount,
                                    "data": {"id": id}}
                    break
                else:
                    ordProduct.sellPrice = ordProduct.product.price
                    order.totalPrice += ordProduct.product.price
            else:
                # 支付订单

                order.receiveAddress = customer.receiveAddresses.get(id=addressId)
                order.payTime = datetime.now()
                order.status = OrderModel.UNSEND
                order.customerMsg = customerMsg
                order.save()
                self.context = {"code": 200, "msg": "订单支付成功", "data": {"id": id}}

    @loginRequire(redirectUrl='/customer/common/login')
    def cancelOrder(self,request):
        """取消订单"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        customer = self.context["customer"]
        order = customer.orders.get(id=id)
        if order.status == OrderModel.UNPAY:
            order.status = OrderModel.CANCEL
            order.cancelTime = datetime.now()
            order.save()
            self.context = {"code":200,"msg":"订单取消成功","data":{"id":id}}
        else:
            self.context = {"code": 4, "msg": "订单取消失败,订单已支付", "data": {"id": id}}