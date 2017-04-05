from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.urls import reverse

from app.views.appbaseview import AppBaseView
from models.carousel import CarouselModel
from models.product import ProductModel
from models.productcategory import ProductCategoryModel
from models.seller import SellerModel


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

    def success(self, request):
        pass

    def introduction(self, request):
        pass

    def order(self, request):
        pass

    def search(self, request):
        """搜索"""
        name = request.GET.get("name")
        if name:
            raw = ProductModel.objects.filter(name__icontains=name,status=ProductModel.ONSHELVE)
            page = request.GET.get("page")
            self.context["productsAmount"] = raw.count()

            if raw:
                self.context["brands"] = [pd.brand for pd in raw[0].category.products.all().only("brand")]
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




    def shopcart(self, request):
        pass

    def activity(self, request):
        pass

    def fail(self, request):
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
