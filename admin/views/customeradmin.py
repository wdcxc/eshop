from util.baseview import BaseView,loginRequire

class CustomerAdminView(BaseView):
    @loginRequire()
    def index(self,request):
        pass