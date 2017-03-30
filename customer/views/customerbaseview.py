from models.customer import CustomerModel
from util.baseview import BaseView


class CustomerBaseView(BaseView):
    def beforeAction(self, request):
        super(CustomerBaseView,self).beforeAction(request)
        if "user" in request.session:
            customer = CustomerModel.objects.get(id=request.session["user"]["id"])
            self.context["customer"] = customer
            self.context["shopcartsNum"] = customer.shopcarts.all().count()
