from util.baseview import BaseView
from app.models import CarouselModel


class CommonView(BaseView):
    def index(self,request):
        """商城首页"""
        self.response_["type"] = self.RESPONSE_TYPE_DEFAULT
        # 轮播图
        carousels = CarouselModel.object.filter(show=True).order_by("-order")
        self.context["carousels"] = []
        for carousel in carousels:
            self.context["carousels"].append({"title":carousel["title"],"imgUrl":carousel["imgUrl"]})

    def success(self,request):
        pass

    def introduction(self,request):
        pass

    def pay(self,request):
        pass

    def search(self,request):
        pass

    def shopcart(self,request):
        pass
