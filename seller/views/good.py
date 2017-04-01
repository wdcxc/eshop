from util.baseview import loginRequire,BaseView

class GoodView(BaseView):
    @loginRequire()
    def goodslist(self,request):
        pass

    @loginRequire()
    def addGood(self,request):
        pass

    @loginRequire()
    def updateGood(self,request):
        pass

    @loginRequire()
    def deleteGood(self,request):
        pass

    @loginRequire()
    def offShelve(self,request):
        pass

