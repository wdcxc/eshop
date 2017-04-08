from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from customer.views.customerbaseview import CustomerBaseView
from util.baseview import loginRequire


class OrderView(CustomerBaseView):
    @loginRequire()
    def order(self, request):
        customer = self.context["customer"]
        allOrders = customer.orders.all().order_by("-addTime")

        paginator = Paginator(allOrders.values(),3)
        page = request.GET.get("page")
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)

        for order in orders:
            order.update({"products":customer.orders.get(id=order["id"]).products.all()})
        self.context["orders"] = orders

