from django.db import models


class ShoppingGuideChannel(models.Model):
    """商城首页商品导购栏目"""
    name = models.CharField(max_length=100)  # 栏目名称
    addTime = models.DateTimeField(auto_now_add=True)  # 栏目添加时间
    addAdminId = models.IntegerField()  # 添加栏目管理员id
    show = models.BooleanField(default=True)  # 是否展示
    order = models.IntegerField(default=1)  # 展示顺序（数字越大，展示越前）

    class Meta:
        db_table = "shoppingguide_channel"


class ShoppingGuideSubchannel(models.Model):
    """商城首页商品导购子栏目"""
    name = models.CharField(max_length=100)  # 子栏目名称
    parentId = models.IntegerField()  # 子栏目归属栏目id
    addTime = models.DateTimeField(auto_now_add=True)  # 栏目添加时间
    addAdminId = models.IntegerField()  # 添加子栏目管理员id
    show = models.BooleanField(default=True)  # 子栏目是否展示
    order = models.IntegerField(default=1)  # 子栏目展示顺序（数字越大，展示越前）

    class Meta:
        db_table = "shoppingguide_subchannel"


class ShoppingGuideProduct(models.Model):
    """商城首页商品导购商品"""
    parentId = models.IntegerField()  # 导购商品归属子栏目id
    name = models.CharField(max_length=50, default="")  # 导购商品名称
    description = models.CharField(max_length=100, default="")  # 商品说明
    linkUrl = models.URLField(default="")  # 商品链接
    productImgUrl = models.URLField(default="")  # 展示图片链接
    addTime = models.DateTimeField(auto_now_add=True)  # 添加时间
    addAdminId = models.IntegerField()  # 添加导购商品管理员id
    show = models.BooleanField(default=True)  # 商品是否展示
    order = models.IntegerField(default=1)  # 商品展示顺序（数字越大，展示越前）

    class Meta:
        db_table = "shoppingguide_product"
