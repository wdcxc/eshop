from models.seller import SellerModel
from util.baseview import BaseView


class SellerBaseView(BaseView):
    def beforeAction(self, request):
        super(SellerBaseView,self).beforeAction(request)
        if "user" in request.session and request.session["user"]["app"] == self.request_["appadmin"]:
            self.context["seller"] = SellerModel.objects.get(id=request.session["user"]["id"])