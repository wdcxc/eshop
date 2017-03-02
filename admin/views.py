from util.baseview import BaseView,loginRequire


class AdminView(BaseView):
    def login(self, request):
        """登录"""
        pass

    @loginRequire()
    def index(self, request):
        """总览"""
        pass

    def logout(self,request):
        pass
