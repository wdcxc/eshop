from app.models import ProductCategoryModel
from util.baseview import BaseView,loginRequire


class ProductAdminView(BaseView):
    @loginRequire()
    def index(self,request):
        pass

    @loginRequire()
    def category(self,request):
        """商品类别管理首页"""
        categories = ProductCategoryModel.objects.all().order_by("-grade","-show","-order","id")
        sortedCategories = self._sortCategories(categories)
        self.context["categories"] = sortedCategories

    @loginRequire()
    def tag(self,request):
        """商品标签管理首页"""
        pass

    @loginRequire()
    def product(self,request):
        """商品管理首页"""
        pass

    @loginRequire()
    def addCategory(self,request):
        """添加商品类别"""
        if request.method == "GET":
            parentId = request.GET.get("parentId",0)
            if parentId:
                parentCategory = ProductCategoryModel.objects.get(id=parentId)
                self.context["category"] = {"parentId":parentId,"grade":parentCategory.grade+1,"order":1}
            else:
                self.context["category"] = {"parentId":parentId,"grade":1,"order":1}
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            categoryKeys = ("parentId","name","grade","show","order")
            category = {}
            for key in categoryKeys:
                category[key] = request.POST.get(key)
            newCategory = ProductCategoryModel(parentId=category["parentId"],name=category["name"],grade=category["grade"],show=category["show"],order=category["order"])
            newCategory.save()
            self.context = {"code":200,"msg":"添加新商品类别成功","data":{"productId":newCategory.id}}

    @loginRequire()
    def updateCategory(self,request):
        """更新商品类别"""
        if request.method == "GET":
            self.context["category"] = ProductCategoryModel.objects.get(id=request.GET.get("id"))
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("id","parentId","name","show","order","grade")
            category = {}
            for key in keys:
                category[key] = request.POST.get(key)
            ProductCategoryModel.objects.filter(id=category["id"]).update(parentId=category["parentId"],name=category["name"],show=category["show"],order=category["order"],grade=category["grade"])
            self.context = {"code":200,"msg":"更新商品目录成功","data":{"id":category["id"]}}

    @loginRequire()
    def deleteCategory(self,request):
        """删除商品类别"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        categoryId = request.POST.get("id")
        if ProductCategoryModel.objects.filter(parentId = categoryId).exists():
            self.context = {"code":4,"msg":"删除商品类别失败，请先删除全部子类别","data":{"categoryId":categoryId}}
        else:
            delete = ProductCategoryModel.objects.get(id=categoryId).delete()
            self.context = {"code": 200, "msg": "删除商品类别成功", "data": {"categoryId": categoryId}}

    def _sortCategories(self,categories):
        """商品类别排序
        python3.4+ 才可用，因为 python3.4+ dict是有序的
        返回一个排序后的列表
        """
        categories = list(categories)
        sortedCategoriesDict = {}
        while categories:
            curGrade = categories[0].grade
            for i,categorie in enumerate(categories):
                if categorie.grade == curGrade:
                    if categorie.parentId in sortedCategoriesDict:
                        sortedCategoriesDict[categorie.parentId].append(categorie)
                    else:
                        sortedCategoriesDict[categorie.parentId] = [categorie]
                    if categorie.id in sortedCategoriesDict:
                        sortedCategoriesDict[categorie.parentId].extend(sortedCategoriesDict[categorie.id])
                        del sortedCategoriesDict[categorie.id]
                    del categories[i]
                else:
                    break
        return list(sortedCategoriesDict.values())[0] if sortedCategoriesDict else []