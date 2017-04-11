from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from customer.views.customerbaseview import CustomerBaseView
from models.customer import Suggestion
from models.order import OrderProductModel
from util.baseview import loginRequire


class ServiceView(CustomerBaseView):
    @loginRequire()
    def suggestion(self, request):
        """意见咨询"""
        pass

    @loginRequire()
    def addSuggestion(self, request):
        """添加意见咨询"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        keys = ("suggestion", "type")
        dict = {}
        for key in keys:
            dict[key] = request.POST.get(key)
        customer = self.context["customer"]
        try:
            suggestion = customer.suggestions.create(**dict)
        except Exception as e:
            self.context = {"code": 4, "msg": "意见提交失败", "data": {"error": str(e)}}
        else:
            self.context = {"code": 200, "msg": "意见提交成功", "data": {"id": suggestion.id}}

    def consult(self, request):
        pass

    def message(self, request):
        pass

    @loginRequire()
    def suggestionMessage(self, request):
        """意见回复"""
        customer = self.context["customer"]
        suggestions = customer.suggestions.filter(reply__isnull=False).order_by("addTime")
        paginator = Paginator(suggestions.values(), 2)
        page = request.GET.get("page")
        try:
            self.context["suggestions"] = paginator.page(page)
        except EmptyPage:
            self.context["suggestions"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["suggestions"] = paginator.page(1)

        suggestionType = {Suggestion.PRODUCT: "产品意见", Suggestion.REFUND: "退款意见", Suggestion.SELLER_SERVICE: "卖家服务",
                          Suggestion.OTHER: "其他意见", Suggestion.PAY: "支付意见"}
        for suggestion in self.context["suggestions"]:
            suggestion["type"] = suggestionType[suggestion["type"]]

    @loginRequire()
    def refundMessage(self, request):
        """退款回复"""
        customer = self.context["customer"]
        ordProducts = OrderProductModel.objects.filter(order__customer=customer, status__in=(
            OrderProductModel.AC_REFUND, OrderProductModel.REFUND, OrderProductModel.RF_REFUND))
        page = request.GET.get("page")
        paginator = Paginator(ordProducts, 2)
        try:
            self.context["refunds"] = paginator.page(page)
        except EmptyPage:
            self.context["refunds"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["refunds"] = paginator.page(1)

        refundStatusDict = {OrderProductModel.REFUND: "等待商家处理", OrderProductModel.AC_REFUND: "商家接受退货",
                            OrderProductModel.RF_REFUND: "商家拒绝退货"}
        for refund in self.context["refunds"]:
            refund.status = refundStatusDict[refund.status]
