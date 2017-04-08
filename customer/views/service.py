from customer.views.customerbaseview import CustomerBaseView
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
