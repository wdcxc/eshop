from util.baseview import BaseView,loginRequire


class IndexView(BaseView):
    @loginRequire()
    def index(self,request):
        pass