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
        page = request.GET.get("page")
        paginator = Paginator(sellers,10)
        try:
            self.context["sellers"] = paginator.page(page)
        except EmptyPage:
            self.context["sellers"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["sellers"] = paginator.page(1)