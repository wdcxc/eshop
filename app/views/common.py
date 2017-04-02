from models.carousel import CarouselModel
from models.productcategory import ProductCategoryModel
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
        # 商品分类导航栏
            productCategories = ProductCategoryModel.objects.all().order_by("-grade","show","-order","-id")
            sortedProductCategories = self._sortProductCategories(productCategories)
            self.context["categories"] = sortedProductCategories

    def success(self,request):
        pass

    def introduction(self,request):
        pass

    def order(self,request):
        pass

    def search(self,request):
        pass

    def shopcart(self,request):
        pass

    def activity(self,request):
        pass

    def fail(self,request):
        pass

    def contact(self,request):
        pass

    def about(self,request):
        pass

    def help(self,request):
        pass

    def _sortProductCategories(self,productCategories):
        categories = list(productCategories.values())
        sortedCategoriesDict = {}
        while categories:
            curGrade = categories[0]["grade"]
            for i,category in enumerate(categories):
                if category["grade"] == curGrade:
                    if category["id"] in sortedCategoriesDict:
                        category.update(sortedCategoriesDict[category["id"]])
                        del sortedCategoriesDict[category["id"]]
                    if category["parentId"] in sortedCategoriesDict:
                        sortedCategoriesDict[category["parentId"]]["subCategories"].append(category)
                    else:
                        sortedCategoriesDict[category["parentId"]] = {"subCategories":[category]}
                    del categories[i]
                else:
                    break
        return sortedCategoriesDict[0]["subCategories"] if sortedCategoriesDict[0] else {}
