from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models.product import ProductImageModel, ProductModel
from models.productcategory import ProductCategoryModel
from models.seller import SellerModel
from seller.views.sellerbaseview import SellerBaseView
from util.baseview import loginRequire
from util.upload import Upload


class GoodView(SellerBaseView):
    @loginRequire()
    def goodslist(self, request):
        categories = ProductCategoryModel.objects.filter(grade=1).only("name", "id")
        self.context["categories"] = categories

        seller = self.context["seller"]
        products = seller.products.all().order_by("-addTime")
        page = request.GET.get("page")
        paginator = Paginator(products,2)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        self.context["products"] = products


    @loginRequire()
    def addGoods(self, request):
        """添加商品"""
        if request.method == "GET":
            g3Category = ProductCategoryModel.objects.get(id=request.GET.get("categoryId"))
            g2Category = ProductCategoryModel.objects.get(id=g3Category.parentId)
            g1Category = ProductCategoryModel.objects.get(id=g2Category.parentId)
            propertyMetas = g3Category.propertyMetas.all()
            self.context["category"] = {"g1": g1Category, "g2": g2Category, "g3": g3Category}
            self.context["propertyMetas"] = propertyMetas
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON

            keys = ("name", "price", "amount", "description", "brand", "status", "categoryId")
            dict = {}
            for key in keys:
                dict[key] = request.POST.get(key)

            category = ProductCategoryModel.objects.get(id=dict["categoryId"])
            del dict["categoryId"]
            dict["category"] = category

            seller = SellerModel.objects.get(id=request.session["user"]["id"])
            dict["seller"] = seller
            if dict["status"] == str(ProductModel.ONSHELVE):
                dict["onShelveTime"] = datetime.now()

            goods = ProductModel(**dict)
            goods.save()

            uploadImageUrls = request.POST.getlist("uploadImages[]")
            for imageUrl in uploadImageUrls:
                goods.images.create(url=imageUrl)

            propertyMetas = category.propertyMetas.all()
            for meta in propertyMetas:
                property = {"meta": meta, "value": request.POST.get("properties[" + str(meta.id) + "]")}
                goods.properties.create(**property)

            self.context = {"code": 200, "msg": "添加商品成功", "data": {"id": goods.id}}

    @loginRequire()
    def updateGoods(self, request):
        pass

    @loginRequire()
    def deleteGoods(self, request):
        pass

    @loginRequire()
    def offShelve(self, request):
        pass

    @loginRequire()
    def uploadImage(self, request):
        """上传商品图片"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        image = request.FILES["productImages"]
        self.context = Upload.uploadImg(dir="product", img=image)

    @loginRequire()
    def deleteImage(self, request):
        """删除商品图片"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        if id:
            ProductImageModel.objects.get(id=id).delete()
            self.context = {"code": 200, "msg": "删除图片成功", "data": {"id": id}}
        self.context = {"code": 4, "msg": "删除图片失败", "data": {}}

    @loginRequire()
    def getSubCategories(self, request):
        """获得商品类别的子类别"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        categories = ProductCategoryModel.objects.filter(parentId=id)
        subCategories = [{"id": category.id, "name": category.name} for category in categories]
        self.context = {"code": 200, "msg": "获取子类别成功", "data": {"subCategories": subCategories}}
