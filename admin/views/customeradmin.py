from  datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from admin.views.adminbaseview import AdminBaseView
from models.customer import CustomerModel
from util.baseview import loginRequire


class CustomerAdminView(AdminBaseView):
    @loginRequire()
    def index(self, request):
        customers = CustomerModel.objects.all().order_by("-registTime")
        name = request.GET.get("name")
        if name:
            customers = customers.filter(name__icontains=name)
        self.context["amount"] = customers.count()
        paginator = Paginator(customers, 10)
        page = request.GET.get("page")
        try:
            self.context["customers"] = paginator.page(page)
        except EmptyPage:
            self.context["customers"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["customers"] = paginator.page(1)

    @loginRequire()
    def lockAccount(self, request):
        """封号"""
        self.response_["type"] =  self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        try:
            customer = CustomerModel.objects.get(id=id)
            customer.lock = True
            customer.lockTime = datetime.now()
            customer.save()
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
            customer = CustomerModel.objects.get(id=id)
            customer.lock = False
            customer.lockTime = datetime.now()
            customer.save()
        except Exception as e:
            self.context = {"code": 4, "msg": "解除封号失败", "data": {"id": id}}
        else:
            self.context = {"code": 200, "msg": "解除封号成功", "data": {"id": id}}
