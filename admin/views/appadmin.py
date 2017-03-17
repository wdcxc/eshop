from django.urls import reverse

from app.models import CarouselModel
from util.baseview import BaseView,loginRequire


class AppAdminView(BaseView):
    def index(self,request):
        pass

    @loginRequire()
    def carousel(self,request):
        """首页轮播管理"""
        self.context["carousels"] = CarouselModel.objects.all().order_by("-order")

    @loginRequire()
    def addCarousel(self,request):
        print("request:",request)
        if request.method == 'POST':
            carouselKeys = ["title","show","order","imgUrl","linkUrl"]
            carousel = {}
            for carouselKey in carouselKeys:
                carousel[carouselKey] = request.POST.get(carouselKey)
            # todo:数据清洗
            newCarousel = CarouselModel(title=carousel["title"],show=carousel["show"],order=carousel["order"],imgUrl=carousel["imgUrl"],linkUrl=carousel["linkUrl"])
            newCarousel.save()
            self.context = {"code":200,"msg":"添加首页轮播图成功","data":{"newCarouselId":newCarousel.id}}
            self.response_["type"] = self.RESPONSE_TYPE_JSON

    @loginRequire()
    def updateCarousel(self,request):
        if request.method == "GET":
            self.context["carousel"] = CarouselModel.objects.get(id=request.GET.get("carouselId"))
        else:
            carouselKeys = ["id","title","show","order","imgUrl","linkUrl"]
            carousel = {}
            for carouselKey in carouselKeys:
                carousel[carouselKey] = request.POST.get(carouselKey)
            CarouselModel.objects.filter(id=carousel["id"]).update(title=carousel["title"],show=carousel["show"],order=carousel["order"],imgUrl=carousel["imgUrl"],linkUrl=carousel["linkUrl"])
            self.context["redirectPath"] = reverse("admin:appAdminCarousel")
            self.response_["type"] = self.RESPONSE_TYPE_REDIRECT

    @loginRequire()
    def deleteCarousel(self,request):
        delete = CarouselModel.objects.get(id=request.GET.get("carouselId")).delete()
        self.context["redirectPath"] = reverse("admin:appAdminCarousel")
        self.response_["type"] = self.RESPONSE_TYPE_REDIRECT