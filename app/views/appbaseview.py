from util.baseview import BaseView


class AppBaseView(BaseView):
    def beforeAction(self, request):
        super(AppBaseView,self).beforeAction(request)
        # if "user" in request.session and request.session["user"]["app"] == self.request_["appadmin"]:
        #     self.context["customer"] = CustomerModel.objects.get(id=)
