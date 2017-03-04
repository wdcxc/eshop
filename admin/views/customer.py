from util.baseview import BaseView,loginRequire

class CustomerView(BaseView):
    @loginRequire()
    def index(self,request):
        pass