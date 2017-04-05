from models.customer import CustomerModel
from util.baseview import BaseView


class CustomerBaseView(BaseView):
    def beforeAction(self, request):
        super(CustomerBaseView, self).beforeAction(request)
        if self.request_["controller"] != "common":
            if "user" in request.session:
                try:
                    customer = CustomerModel.objects.get(id=request.session["user"]["id"])
                except CustomerModel.DoesNotExist:
                    self.response_["type"] = self.RESPONSE_TYPE_REDIRECT
                    self.context["redirectPath"] = "/customer/common/login"
                    return self.afterAction(request)
                else:
                    self.context["customer"] = customer
                    self.context["shopcartsNum"] = customer.shopcarts.all().count()
            else:
                self.response_["type"] = self.RESPONSE_TYPE_REDIRECT
                self.context["redirectPath"] = "/customer/common/login"
                return self.afterAction(request)