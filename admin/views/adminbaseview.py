from django.urls import reverse

from models.admin import AdminModel
from util.baseview import BaseView


class AdminBaseView(BaseView):
    def beforeAction(self, request):
        super(AdminBaseView, self).beforeAction(request)
        if self.request_["controller"] != "common":
            if "user" in request.session:
                admin = AdminModel.objects.get(id=request.session["user"]["id"])
                if not admin.root:
                    groups = admin.groups.all()
                    nodes = {node.linkUrl: node for group in groups for node in group.nodes.all()}
                    requestPath = "/" + self.request_["appadmin"] + "/" + self.request_["controller"] + "/" + self.request_["action"]
                    if requestPath not in nodes:
                        self.response_["type"] = self.RESPONSE_TYPE_REDIRECT
                        self.context["redirectPath"] = reverse("admin:forbidden")
                        return self.afterAction(request)

    def afterAction(self, request):
        return super(AdminBaseView, self).afterAction(request)
