from collections import OrderedDict

from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.urls import reverse

from app.views.appbaseview import AppBaseView
from models.carousel import CarouselModel
from models.order import OrderProductModel, OrderModel
from models.product import ProductModel
from models.productcategory import ProductCategoryModel
from models.seller import SellerModel
from models.shoppingguide import ShoppingGuideChannel, ShoppingGuideSubchannel, ShoppingGuideProduct
from util.baseview import loginRequire


class CommonView(AppBaseView):
    def index(self, request):
        """商城首页"""
        self.response_["type"] = self.RESPONSE_TYPE_DEFAULT
        # 轮播图
        carousels = CarouselModel.objects.filter(show=True).order_by("-order")
        self.context["carousels"] = []
        self.context["carouselsCount"] = range(len(carousels))
        for carousel in carousels:
            self.context["carousels"].append(
                {"title": carousel.title, "imgUrl": carousel.imgUrl, "linkUrl": carousel.linkUrl})
        # 商品分类导航栏
        productCategories = ProductCategoryModel.objects.all().order_by("-grade", "show", "-order", "-id")
        sortedProductCategories = self._sortProductCategories(productCategories)
        self.context["categories"] = sortedProductCategories
        # 商品导购
        guideChannels = ShoppingGuideChannel.objects.filter(show=True).order_by("-order")
        guideSubChannels = ShoppingGuideSubchannel.objects.filter(show=True).order_by("-order")
        guideProducts = ShoppingGuideProduct.objects.filter(show=True).order_by("-order")
        self.context["channels"] = self._sortShoppingGuide(guideChannels, guideSubChannels, guideProducts)

    @loginRequire(redirectUrl='/customer/common/login')
    def introduction(self, request):
        """商品详情页"""
        try:
            product = ProductModel.objects.get(id=request.GET.get("id"))
        except Exception as e:
            print(e)
        product.__dict__.update({
            "images": product.images.all()[:4],
            "detailImages":product.images.all(),
            "properties": product.properties.all(),
            "category": product.category,
        })
        if product.images.all():
            product.__dict__.update({"firstImage": product.__dict__["images"][0]})
        self.context["product"] = product.__dict__

        collection = self.context["customer"].collections.filter(product=product)
        if collection.exists():
            self.context["collection"] = collection[0]

        # 评价
        evaluations = product.ordProducts.filter(evaluation__isnull=False).order_by("-evaluateTime")
        self.context["total"] = evaluations.count()
        self.context["good"] = evaluations.filter(eGrade=OrderProductModel.GOOD).count()
        self.context["middle"] = evaluations.filter(eGrade=OrderProductModel.MIDDLE).count()
        self.context["bad"] = evaluations.filter(eGrade=OrderProductModel.BAD).count()
        self.context["goodpercent"] = 100 if not self.context["total"] else self.context["good"] / self.context[
            "total"] * 100
        page = request.GET.get("page")
        paginator = Paginator(evaluations, 10)
        try:
            self.context["evaluations"] = paginator.page(page)
        except EmptyPage:
            self.context["evaluations"] = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            self.context["evaluations"] = paginator.page(1)

        # 同类商品推荐
        self.context["recmandProducts"] = ProductModel.objects.filter(category=product.category).exclude(id=product.id)[
                                          :2]

    def search(self, request):
        """搜索"""
        name = request.GET.get("name")
        raw = None
        if name:
            raw = ProductModel.objects.filter(name__icontains=name, status=ProductModel.ONSHELVE)
            self.context["name"] = name
        brand = request.GET.get("brand")
        if brand:
            raw = raw.filter(brand=brand)
        categoryId = request.GET.get("category_id")
        if categoryId:
            if raw:
                raw = raw.filter(category=ProductCategoryModel.objects.get(id=categoryId))
            else:
                raw = ProductModel.objects.filter(category=ProductCategoryModel.objects.get(id=categoryId), status=ProductModel.ONSHELVE)
        order = request.GET.get("method")
        if order:
            if order == "price":
                raw = raw.order_by(order)
            elif order == "number":
                raw = raw.order_by("-" + "soldoutAmount")

        page = request.GET.get("page")

        if raw:
            self.context["productsAmount"] = raw.count()
            self.context["brands"] = [pd.brand for pd in raw[0].category.products.distinct("brand")]
            self.context["categories"] = ProductCategoryModel.objects.filter(parentId=raw[0].category.parentId)

            paginator = Paginator(raw.values(), 8)
            try:
                products = paginator.page(page)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                products = paginator.page(1)

            for product in products:
                try:
                    product["image"] = ProductModel.objects.get(id=product["id"]).images.all()[0]
                except:
                    pass
                product["seller"] = SellerModel.objects.get(id=product["seller_id"])

            self.context["products"] = products

    @loginRequire(redirectUrl='/customer/common/login')
    def shopcart(self, request):
        """购物车"""
        self.context["shopcarts"] = self.context["customer"].shopcarts.all()

    @loginRequire(redirectUrl='/customer/common/login')
    def addShopcart(self, request):
        """添加购物车"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        num = request.GET.get("num")
        try:
            customer = self.context["customer"]
            product = ProductModel.objects.get(id=id)
            customer.shopcarts.create(product=product, amount=num)
        except Exception as e:
            self.context = {"code": 4, "msg": "添加购物车失败", "data": {"pid": id, "error": str(e)}}
        else:
            self.context = {"code": 200, "msg": "添加购物车成功", "data": {"pid": id}}

    @loginRequire(redirectUrl='/customer/common/login')
    def buynow(self, request):
        """立即购买"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        id = request.GET.get("id")
        num = request.GET.get("num")
        try:
            customer = self.context["customer"]
            product = ProductModel.objects.get(id=id)
            newOrder = OrderModel(customer=customer)
            newOrder.save()
            newOrder.products.create(product=product, amount=num)
        except Exception as e:
            self.context = {"code": 4, "msg": "下单失败", "data": {"pid": id, "error": str(e)}}
        else:
            self.context = {"code": 200, "msg": "下单成功", "data": {"oid": newOrder.id}}

    @loginRequire(redirectUrl='/customer/common/login')
    def deleteShopcart(self, request):
        """删除购物车"""
        try:
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            id = request.GET.get("id")
            customer = self.context["customer"]
            customer.shopcarts.get(id=id).delete()
            self.context = {"code": 200, "msg": "删除购物车商品成功", "data": {"id": id}}
        except Exception as e:
            self.context = {"code": 4, "msg": "删除购物车商品失败", "data": {"id": id, "error": str(e)}}

    def activity(self, request):
        pass

    def contact(self, request):
        pass

    def about(self, request):
        pass

    def help(self, request):
        pass

    def logout(self, request):
        """退出登陆"""
        self.response_["type"] = self.RESPONSE_TYPE_REDIRECT
        if "user" in request.session:
            del request.session["user"]
        if "customer" in self.context:
            del self.context["customer"]
        self.context["redirectPath"] = reverse("app:index")

    def _sortProductCategories(self, productCategories):
        """商品目录排序"""
        categories = list(productCategories.values())
        sortedCategoriesDict = {}
        while categories:
            curGrade = categories[0]["grade"]
            for i, category in enumerate(categories):
                if category["grade"] == curGrade:
                    if category["id"] in sortedCategoriesDict:
                        category.update(sortedCategoriesDict[category["id"]])
                        del sortedCategoriesDict[category["id"]]
                    if category["parentId"] in sortedCategoriesDict:
                        sortedCategoriesDict[category["parentId"]]["subCategories"].append(category)
                    else:
                        sortedCategoriesDict[category["parentId"]] = {"subCategories": [category]}
                    del categories[i]
                else:
                    break
        return sortedCategoriesDict[0]["subCategories"] if sortedCategoriesDict[0] else {}

    @loginRequire()
    def addCollection(self, request):
        """添加收藏"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        pid = request.GET.get("pid")
        product = ProductModel.objects.get(id=pid)
        customer = self.context["customer"]
        if customer.collections.filter(product=product).exists():
            self.context = {"code": 4, "msg": "商品已被收藏", "data": {"id": pid}}
        else:
            try:
                collection = customer.collections.create(product=product)
            except Exception:
                self.context = {"code": 4, "msg": "收藏商品失败", "data": {"id": pid}}
            else:
                self.context = {"code": 200, "msg": "收藏商品成功", "data": {"id": collection.id}}

    @loginRequire()
    def deleteCollection(self, request):
        """取消收藏"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        cid = request.GET.get("id")
        customer = self.context["customer"]
        try:
            collection = customer.collections.get(id=cid)
        except Exception as e:
            self.context = {"code": 4, "msg": "取消收藏失败", "data": {"id": cid}}
            print(e)
        else:
            collection.delete()
            self.context = {"code": 200, "msg": "商品已取消收藏", "data": {"id": cid}}

    def _sortShoppingGuide(self, channels, subChannels, products):
        """商品导购排序"""
        channels = list(channels.values())
        subChannels = list(subChannels.values())
        products = list(products.values())

        subChannelsDict = OrderedDict({subChannel["id"]: subChannel for subChannel in subChannels})
        for product in products:
            if "products" not in subChannelsDict[product["parentId"]]:
                subChannelsDict[product["parentId"]]["products"] = []
            subChannelsDict[product["parentId"]]["products"].append(product)

        channelsDict = OrderedDict({channel["id"]: channel for channel in channels})
        for subChannel in subChannelsDict.values():
            if "subChannels" not in channelsDict[subChannel["parentId"]]:
                channelsDict[subChannel["parentId"]]["subChannels"] = []
            channelsDict[subChannel["parentId"]]["subChannels"].append(subChannel)

        return list(channelsDict.values())
