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
        paginator = Paginator(customers, 10)
        page = request.GET.get("page")
        try:
            self.context["customers"] = paginator.page(page)
        except EmptyPage:
            self.context["customers"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["customers"] = paginator.page(1)
