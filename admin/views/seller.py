from util.baseview import BaseView,loginRequire

class SellerView(BaseView):
    @loginRequire()
    def index(self,request):
        pass