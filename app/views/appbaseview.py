from models.customer import CustomerModel
from util.baseview import BaseView


class AppBaseView(BaseView):
    def beforeAction(self, request):
        super(AppBaseView, self).beforeAction(request)
        if "user" in request.session:
            self.context["customer"] = CustomerModel.objects.get(id=request.session["user"]["id"])
