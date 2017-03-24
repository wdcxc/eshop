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
        self.context = self._uploadImg(img,"carousel")

    @loginRequire()
    def updateCarouselImg(self,request):
        """更新上传的轮播图"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        newImg = request.FILES["newImg"]
        oldImgUrl = request.POST.get("oldImgUrl")
        # todo:删除旧的图片
        self.context = self.uploadImg(newImg)

    def _uploadImg(self,img,dir):
        """上传图片"""
        result = {}
        allowUploadType = ("image/jpg", "image/jpeg", "image/png", "image/gif")
        if img.content_type not in allowUploadType:
            result = {"code": 4, "msg": "上传文件格式错误", "data": {"imagetype": img.content_type}}
        elif img.size >= 10 * 1024 * 1024:
            result = {"code": 4, "msg": "上传文件过大", "data": {"imagesize": img.size}}
        else:
            curdate = datetime.strftime(datetime.date(datetime.now()), "%Y%M%d")
            imgSaveDir = os.path.normpath(settings.BASE_DIR + settings.MEDIA_ROOT + "/"+dir+"/" + curdate)
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
    def deleteShoppingGuideChannel(self,request):
        """删除商品导购栏目"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        channelId = request.POST.get("id")
        if ShoppingGuideSubchannel.objects.filter(parentId=channelId).exists():
            self.context = {"code": 4, "msg": "请先删除所有子栏目", "data": {"id":channelId}}
        else:
            ShoppingGuideChannel.objects.get(id=channelId).delete()
            self.context = {"code":200,"msg":"删除商品导购栏目成功","data":{"id":channelId}}

    @loginRequire()
    def updateShoppingGuideChannel(self,request):
        """更新商品导购栏目"""
        if request.method == "GET":
            self.context["channel"] = ShoppingGuideChannel.objects.get(id=request.GET.get("id"))
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("id","name","show","order")
            vals = {}
            for key in keys:
                vals[key] = request.POST.get(key)
            channel = ShoppingGuideChannel.objects.get(id=vals["id"])
            channel.name = vals["name"]
            channel.show = vals["show"]
            channel.order = vals["order"]
            channel.save()
            self.context = {"code":200,"msg":"更新商品导购栏目成功","data":{"id":channel.id}}

    @loginRequire()
    def addShoppingGuideSubchannel(self,request):
        if request.method == "GET":
            parent = ShoppingGuideChannel.objects.get(id=request.GET.get("id"))
            self.context["parent"] = parent
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("parentId","name","show","order")
            subChannel = {}
            for key in keys:
                subChannel[key] = request.POST.get(key)
            subChannel["addAdminId"] = request.session["user"]["id"]
            newSubchannel = ShoppingGuideSubchannel(parentId=subChannel["parentId"],name=subChannel["name"],show=subChannel["show"],order=subChannel["order"],addAdminId=subChannel["addAdminId"])
            newSubchannel.save()
            self.context = {"code":200,"msg":"成功添加新子栏目","data":{"subChannelId":newSubchannel.id}}

    @loginRequire()
    def deleteShoppingGuideSubchannel(self,request):
        """删除商品导购子栏目"""
        if request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            subChannelId = request.POST.get("id")
            if ShoppingGuideProduct.objects.filter(parentId=subChannelId).exists():
                self.context = {"code":4,"msg":"请先删除子栏目下所有导购商品","data":{"id":subChannelId}}
            else:
                ShoppingGuideSubchannel.objects.get(id=request.POST.get("id")).delete()
                self.context = {"code":200,"msg":"删除子栏目成功","data":{}}

    @loginRequire()
    def updateShoppingGuideSubchannel(self,request):
        """修改商品导购子栏目"""
        if request.method == "GET":
            self.context["subChannel"] = ShoppingGuideSubchannel.objects.get(id=request.GET.get("id"))
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("id","name","show","order")
            vals = {}
            for key in keys:
                vals[key] = request.POST.get(key)
            subChannel = ShoppingGuideSubchannel.objects.get(id=vals["id"])
            subChannel.name = vals["name"]
            subChannel.show = vals["show"]
            subChannel.order = vals["order"]
            subChannel.save()
            self.context = {"code":200,"msg":"更新商品导购子栏目成功","data":{"id":subChannel.id}}

    @loginRequire()
    def addShoppingGuideProduct(self,request):
        """添加导购商品"""
        if request.method == "GET":
            self.context["subChannel"] = ShoppingGuideSubchannel.objects.get(id=request.GET.get("id"))
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("name","linkUrl","productImgUrl","show","order","parentId","description")
            vals = {}
            for key in keys:
                vals[key] = request.POST.get(key)
            vals["addAdminId"] = request.session["user"]["id"]
            print(vals)
            product = ShoppingGuideProduct(name=vals["name"],parentId=vals["parentId"],linkUrl=vals["linkUrl"],productImgUrl=vals["productImgUrl"],show=vals["show"],order=vals["order"],description=vals["description"],addAdminId=vals["addAdminId"])
            product.save()
            self.context = {"code":200,"msg":"添加展示商品成功","data":{"id":product.id}}

    @loginRequire()
    def uploadShoppingGuideProductImg(self,request):
        """上传导购商品图片"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        img = request.FILES["productImg"]
        self.context = self._uploadImg(img,"shoppingguide")

    @loginRequire()
    def deleteShoppingGuideProduct(self,request):
        """删除导购商品"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        productId = request.POST.get("id")
        ShoppingGuideProduct.objects.get(id=productId).delete()
        self.context = {"code":200,"msg":"删除导购商品成功","data":{"id":productId}}

    @loginRequire()
    def updateShoppingGuideProduct(self,request):
        """修改导购商品"""
        if request.method == "GET":
            productId = request.GET.get("id")
            self.context["product"] = ShoppingGuideProduct.objects.get(id=productId)
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("id","name","description","linkUrl","productImgUrl","show","order")
            vals = {}
            for key in keys:
                vals[key] = request.POST.get(key)
            product = ShoppingGuideProduct.objects.get(id=vals["id"])
            product.name = vals["name"]
            product.description = vals["description"]
            product.linkUrl = vals["linkUrl"]
            product.productImgUrl = vals["productImgUrl"]
            product.show = vals["show"]
            product.order = vals["order"]
            product.save()
            self.context = {"code":200,"msg":"修改导购商品成功","data":{"id":product.id}}

    @loginRequire()
    def updateShoppingGuideProductImg(self, request):
        """更新导购商品图片"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        # todo:删除前一张展示图片
        img = request.FILES["productImg"]
        self.context = self._uploadImg(img, "shoppingguide")

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
