from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from customer.views.customerbaseview import CustomerBaseView
from models.order import OrderModel
from util.baseview import loginRequire


class OrderView(CustomerBaseView):
    @loginRequire()
    def receiveorder(self, request):
        pass

    @loginRequire()
    def evaluateorder(self, request):
        pass

    @loginRequire()
    def order(self, request):
        customer = self.context["customer"]
        orders = customer.orders.filter(status=OrderModel.UNSEND).order_by("-addTime")

        paginator = Paginator(orders.values(), 2)
        page = request.GET.get("page")
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)

        for order in orders:
            order.update({"products": customer.orders.get(id=order["id"]).products.all()})
        self.context["orders"] = orders
