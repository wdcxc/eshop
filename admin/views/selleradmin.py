from util.baseview import BaseView,loginRequire

class SellerAdminView(BaseView):
    @loginRequire()
    def index(self,request):
        pass