from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

from customer.views.customerbaseview import CustomerBaseView
from util.baseview import loginRequire


class CollectionView(CustomerBaseView):
    @loginRequire()
    def collection(self, request):
        customer = self.context["customer"]
        collections = customer.collections.all().order_by("-addTime")
        paginator = Paginator(collections, 4)
        page = request.GET.get("page")
        try:
            collections = paginator.page(page)
        except EmptyPage:
            collections = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            collections = paginator.page(1)
        self.context["collections"] = collections
