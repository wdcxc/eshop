from models.order import OrderProductModel
from seller.views.sellerbaseview import SellerBaseView
from util.baseview import loginRequire


class OrderView(SellerBaseView):
    @loginRequire()
    def order(self, request):
        """订单首页"""
        pass

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
