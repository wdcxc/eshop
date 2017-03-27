from admin.views.adminbaseview import AdminBaseView
from util.baseview import loginRequire


class CustomerAdminView(AdminBaseView):
    @loginRequire()
    def index(self,request):
        pass