from util.baseview import BaseView,loginRequire
from app.models import CarouselModel
from django.urls import reverse

class AppAdminView(BaseView):
    def index(self,request):
        pass

    @loginRequire()
    def carousel(self,request):
        """首页轮播管理"""
        self.context["carousels"] = CarouselModel.objects.all().order_by("-order")

    @loginRequire()
    def addCarousel(self,request):
        pass
        # todo
