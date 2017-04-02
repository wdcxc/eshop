from models.seller import SellerModel
from util.baseview import BaseView


class SellerBaseView(BaseView):
    def beforeAction(self, request):
        super(SellerBaseView,self).beforeAction(request)
        if "user" in request.session:
            self.context["seller"] = SellerModel.objects.get(id=request.session["user"]["id"])