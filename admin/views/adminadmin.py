from util.baseview import BaseView,loginRequire


class AdminAdminView(BaseView):
    @loginRequire()
    def index(self,request):
        pass

    def addAdmin(self,request):
        pass

    def deleteAdmin(self,request):
        pass