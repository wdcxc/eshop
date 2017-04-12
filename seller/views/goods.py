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
        """商品列表"""
        categories = ProductCategoryModel.objects.filter(grade=1).only("name", "id")
        self.context["categories"] = categories

        seller = self.context["seller"]
        products = seller.products.all().order_by("-addTime")
        withImageProducts = []
        for product in products:
            try:
                product.__dict__.update({"image": product.images.all()[0]})
            except Exception as e:
                print(e)
            finally:
                withImageProducts.append(product.__dict__)

        page = request.GET.get("page")
        paginator = Paginator(withImageProducts, 5)
        try:
            withImageProducts = paginator.page(page)
        except PageNotAnInteger:
            withImageProducts = paginator.page(1)
        except EmptyPage:
            withImageProducts = paginator.page(paginator.num_pages)
        self.context["products"] = withImageProducts

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

            keys = ("name", "price", "amount", "description", "brand", "status", "categoryId","thumbnail")
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

            try:
                goods = ProductModel(**dict)
                goods.save()
            except Exception as e:
                self.context = {"code": 4, "msg": "请输入有效信息", "data": {"error": str(e)}}
            else:
                uploadImageIds = request.POST.getlist("uploadImages[]")
                for imageId in uploadImageIds:
                    goods.images.add(ProductImageModel.objects.get(id=imageId))

                propertyMetas = category.propertyMetas.all()
                for meta in propertyMetas:
                    property = {"meta": meta, "value": request.POST.get("properties[" + str(meta.id) + "]")}
                    goods.properties.create(**property)

                self.context = {"code": 200, "msg": "添加商品成功", "data": {"id": goods.id}}

    @loginRequire()
    def updateGoods(self, request):
        """修改商品信息"""
        if request.method == "GET":
            product = self.context["seller"].products.get(id=request.GET.get("id"))
            self.context["product"] = product

            g3Category = product.category
            g2Category = ProductCategoryModel.objects.get(id=g3Category.parentId)
            g1Category = ProductCategoryModel.objects.get(id=g2Category.parentId)
            self.context["category"] = {"g1": g1Category, "g2": g2Category, "g3": g3Category}

            self.context["images"] = [{"id": image.id, "url": image.url} for image in product.images.all()]

            self.context["properties"] = product.properties.all()
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON

            product = self.context["seller"].products.filter(id=request.POST.get('id'))
            keys = ("name", "price", "amount", "brand", "status", "description","thumbnail")
            dict = {}
            for key in keys:
                dict[key] = request.POST.get(key)
            product.update(**dict)
            product = product[0]

            if product.status == ProductModel.ONSHELVE:
                product.onShelveTime = datetime.now()
            elif product.status == ProductModel.offShelveTime:
                product.offShelveTime = datetime.now()
            product.save()

            for property in product.properties.all():
                property.value = request.POST.get("properties[" + str(property.id) + "]")
                property.save()

            for imgId in request.POST.getlist("uploadImages[]"):
                product.images.add(ProductImageModel.objects.get(id=imgId))

            self.context = {"code": 200, "msg": "修改商品信息成功", "data": {"id": product.id}}

    @loginRequire()
    def deleteGoods(self, request):
        """删除商品"""
        self.response_['type'] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        seller = self.context["seller"]
        try:
            seller.products.filter(id=id).delete()
        except Exception as e:
            print(e)
            self.context = {"code": 4, "msg": "删除商品失败", "data": {"id": id}}
        else:
            self.context = {"code": 200, "msg": "删除商品成功", "data": {"id": id}}

    @loginRequire()
    def updateStatus(self, request):
        """修改商品状态"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        seller = self.context["seller"]
        product = seller.products.get(id=request.GET.get("id"))
        product.status = request.GET.get("status")
        product.save()
        self.context = {"code": 200, "msg": "修改商品状态成功", "data": {"id": product.id}}

    @loginRequire()
    def uploadImage(self, request):
        """上传商品图片"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        image = request.FILES["productImages"]
        storeRes = Upload.uploadImg(dir="product", img=image)
        if storeRes["code"] == 200:
            img = ProductImageModel(name=image.name, url="/static/media/fileupload/" + storeRes["data"]["imgUrl"])
            img.save()
            storeRes.update(
                {"initialPreview": [img.url], "initialPreviewConfig": [{"key": img.id, "caption": img.name}],
                 "id": img.id,"imgUrl":img.url})
            self.context = storeRes
        else:
            self.context = storeRes

    @loginRequire()
    def deleteImage(self, request):
        """删除商品图片"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        if request.method == "GET":
            id = request.GET.get("key")
        elif request.method == "POST":
            id = request.POST.get("key")
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
