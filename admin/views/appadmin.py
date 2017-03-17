import os
from datetime import datetime

from django.conf import settings
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
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            carouselKeys = ["id","title","show","order","imgUrl","linkUrl"]
            carousel = {}
            for carouselKey in carouselKeys:
                carousel[carouselKey] = request.POST.get(carouselKey)
            print(carousel)
            CarouselModel.objects.filter(id=carousel["id"]).update(title=carousel["title"],show=carousel["show"],order=carousel["order"],imgUrl=carousel["imgUrl"],linkUrl=carousel["linkUrl"])
            self.context = {"code":200,"msg":"更新轮播图成功","data":{}}

    @loginRequire()
    def deleteCarousel(self,request):
        delete = CarouselModel.objects.get(id=request.GET.get("carouselId")).delete()
        self.context["redirectPath"] = reverse("admin:appAdminCarousel")
        self.response_["type"] = self.RESPONSE_TYPE_REDIRECT

    @loginRequire()
    def uploadCarouselImg(self,request):
        """保存上传的轮播图"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        img = request.FILES["img"]
        self.context = self.uploadImg(img)

    @loginRequire()
    def updateCarouselImg(self,request):
        """更新上传的轮播图"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        newImg = request.FILES["newImg"]
        oldImgUrl = request.POST.get("oldImgUrl")
        # todo:删除旧的图片
        self.context = self.uploadImg(newImg)

    def uploadImg(self,img):
        result = {}
        allowUploadType = ("image/jpg", "image/jpeg", "image/png", "image/gif")
        if img.content_type not in allowUploadType:
            result = {"code": 4, "msg": "上传文件格式错误", "data": {"imagetype": img.content_type}}
        elif img.size >= 10 * 1024 * 1024:
            result = {"code": 4, "msg": "上传文件过大", "data": {"imagesize": img.size}}
        else:
            curdate = datetime.strftime(datetime.date(datetime.now()), "%Y%M%d")
            imgSaveDir = os.path.normpath(settings.BASE_DIR + settings.MEDIA_ROOT + "/carousel/" + curdate)
            if not os.path.exists(imgSaveDir):
                os.makedirs(imgSaveDir)
            imgSavePath = os.path.normpath(imgSaveDir + "/" + img.name)
            with open(imgSavePath, "wb") as destination:
                for chunk in img.chunks():
                    destination.write(chunk)
            result = {"code": 200, "msg": "上传文件成功", "data": {"imgUrl": curdate + "/" + img.name}}
        return result