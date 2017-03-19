from app.models import CarouselModel
from util.baseview import BaseView


class CommonView(BaseView):
    def index(self,request):
        """商城首页"""
        self.response_["type"] = self.RESPONSE_TYPE_DEFAULT
        # 轮播图
        carousels = CarouselModel.objects.filter(show=True).order_by("-order")
        self.context["carousels"] = []
        self.context["carouselsCount"] = range(len(carousels))
        for carousel in carousels:
            self.context["carousels"].append({"title":carousel.title,"imgUrl":carousel.imgUrl,"linkUrl":carousel.linkUrl})
        # 分类导航栏

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
