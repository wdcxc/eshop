from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from admin.views.adminbaseview import AdminBaseView
from models.seller import SellerModel
from util.baseview import loginRequire


class SellerAdminView(AdminBaseView):
    @loginRequire()
    def index(self,request):
        sellers = SellerModel.objects.all().order_by("-registTime")
        name = request.GET.get("name")
        if name:
            sellers = sellers.filter(name__icontains=name)
        self.context["amount"] = sellers.count()
        page = request.GET.get("page")
        paginator = Paginator(sellers,10)
        try:
            self.context["sellers"] = paginator.page(page)
        except EmptyPage:
            self.context["sellers"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["sellers"] = paginator.page(1)

    @loginRequire()
    def lockAccount(self, request):
        """封号"""
        self.response_["type"] =  self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        try:
            seller = SellerModel.objects.get(id=id)
            seller.lock = True
            seller.lockTime = datetime.now()
            seller.save()
        except Exception as e:
            self.context = {"code": 4, "msg": "封号失败", "data": {"id": id}}
        else:
            self.context = {"code": 200, "msg": "封号成功", "data": {"id": id}}

    @loginRequire()
    def unlockAccount(self, request):
        """解除封号"""
        self.response_["type"] =  self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        try:
            seller = SellerModel.objects.get(id=id)
            seller.lock = False
            seller.lockTime = datetime.now()
            seller.save()
        except Exception as e:
            self.context = {"code": 4, "msg": "解除封号失败", "data": {"id": id}}
        else:
            self.context = {"code": 200, "msg": "解除封号成功", "data": {"id": id}}