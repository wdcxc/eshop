from customer.views.customerbaseview import CustomerBaseView
from util.baseview import loginRequire


class OrderView(CustomerBaseView):
    @loginRequire()
    def order(self, request):
        pass

    @loginRequire()
    def address(self, request):
        pass
