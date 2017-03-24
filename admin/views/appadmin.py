import os
from datetime import datetime

from django.conf import settings
from django.urls import reverse

from models.carousel import CarouselModel
from models.productcategory import ProductCategoryModel
from models.shoppingguide import ShoppingGuideChannel,ShoppingGuideSubchannel,ShoppingGuideProduct
from util.baseview import BaseView,loginRequire


class AppAdminView(BaseView):
    """商城管理"""

    def index(self,request):
        """商城管理后台首页"""
        pass

    @loginRequire()
    def carousel(self,request):
        """首页轮播管理"""
        self.context["carousels"] = CarouselModel.objects.all().order_by("-order")

    @loginRequire()
    def addCarousel(self,request):
        """新增首页轮播图"""
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
        """更新首页轮播图"""
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
        """删除首页轮播图"""
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

    @loginRequire()
    def productCategory(self,request):
        """更新商城首页商品目录导航"""
        if request.method == "GET":
            productCategories = ProductCategoryModel.objects.all().order_by("-grade","show","-order","-id")
            sortedProductCategories = self._sortProductCategories(productCategories)
            self.context["categories"] = sortedProductCategories
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            changes = request.POST
            showChange = {}
            orderChange = {}
            for k,v in changes.items():
                if k.startswith("s"):
                    showChange[k[2:-1]] = v
                elif k.startswith("o"):
                    orderChange[k[2:-1]] = v
            for id,val in showChange.items():
                productCategory = ProductCategoryModel.objects.get(id=id)
                productCategory.show = val
                productCategory.save()
            for id,val in orderChange.items():
                productCategory = ProductCategoryModel.objects.get(id=id)
                productCategory.order = val
                productCategory.save()
            self.context = {"code":200,"msg":"首页商品目录导航更新成功","data":{}}

    @loginRequire()
    def activity(self,request):
        """商城首页活动管理"""
        # todo
        pass

    @loginRequire()
    def shoppingGuide(self,request):
        """商城首页导购管理"""
        channels = ShoppingGuideChannel.objects.all()
        subChannels = ShoppingGuideSubchannel.objects.all()
        products = ShoppingGuideProduct.objects.all()
        self.context["channels"] = self._sortShoppingGuide(channels,subChannels,products)


    @loginRequire()
    def addShoppingGuideChannel(self,request):
        """添加商城首页商品导购栏目"""
        if request.method == "GET":
            pass
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("name","show","order")
            channel = {}
            for key in keys:
                channel[key] = request.POST.get(key)
            newChannel = ShoppingGuideChannel(name=channel["name"],show=channel["show"],order=channel["order"],addAdminId=request.session["user"]["id"])
            newChannel.save()
            self.context = {"code":200,"msg":"添加新导购栏目成功","data":{"id":newChannel.id}}

    @loginRequire()
    def addShoppingGuideSubchannel(self,request):
        pass

    @loginRequire()
    def addShoppingGuideProduct(self,request):
        pass

    def _sortProductCategories(self,productCategories):
        """商品类别排序
        python3.4+ 有效，dict 在 python3.4+ 是有序的
        """
        productCategories = list(productCategories.values())
        sortedProductCategoriesDict = {}
        while productCategories:
            curGrade = productCategories[0]["grade"]
            for i,productCategory in enumerate(productCategories):
                if productCategory["grade"] == curGrade:
                    if productCategory["id"] in sortedProductCategoriesDict:
                        productCategory.update(sortedProductCategoriesDict[productCategory["id"]])
                        del sortedProductCategoriesDict[productCategory["id"]]
                    if productCategory["parentId"] in sortedProductCategoriesDict:
                        sortedProductCategoriesDict[productCategory["parentId"]]["subCategories"].append(productCategory)
                    else:
                        sortedProductCategoriesDict[productCategory["parentId"]] = {"subCategories":[productCategory]}
                    del productCategories[i]
                else:
                    break
        return sortedProductCategoriesDict[0]["subCategories"] if sortedProductCategoriesDict else []


    def _sortShoppingGuide(self,channels,subChannels,products):
        """商品导购排序"""
        channels = list(channels.values())
        subChannels = list(subChannels.values())
        products = list(products.values())

        subChannelsDict = {subChannel["id"]:subChannel for subChannel in subChannels}
        for product in products:
            if "products" not in subChannelsDict[product["parentId"]]:
                subChannelsDict[product["parentId"]]["products"] = []
            subChannelsDict[product["parentId"]]["products"].append(product)

        channelsDict = {channel["id"]:channel for channel in channels}
        for subChannel in subChannelsDict.values():
            if "subChannels" not in channelsDict[subChannel["parentId"]]:
                channelsDict[subChannel["parentId"]]["subChannels"] = []
            channelsDict[subChannel["parentId"]]["subChannels"].append(subChannel)

        return list(channelsDict.values())
