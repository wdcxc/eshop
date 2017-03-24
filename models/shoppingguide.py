from django.db import models

class ShoppingGuideChannel(models.Model):
    """商城首页商品导购栏目"""
    class Meta:
        db_table = "shoppingguide_channel"

    name = models.CharField(max_length = 100) # 栏目名称
    addTime = models.DateTimeField(auto_now_add=True) # 栏目添加时间
    addAdminId = models.IntegerField() # 添加栏目管理员id
    show = models.BooleanField(default = True) # 是否展示
    order = models.IntegerField(default = 1) # 展示顺序（数字越大，展示越前）

class ShoppingGuideSubchannel(models.Model):
    """商城首页商品导购子栏目"""
    class Meta:
        db_table = "shoppingguide_subchannel"

    name = models.CharField(max_length=100) # 子栏目名称
    parentId = models.IntegerField() # 子栏目归属栏目id
    addTime = models.DateTimeField(auto_now_add=True) # 栏目添加时间
    addAdminId = models.IntegerField() # 添加子栏目管理员id
    show = models.BooleanField(default = True) # 子栏目是否展示
    order = models.IntegerField(default = 1) # 子栏目展示顺序（数字越大，展示越前）

class ShoppingGuideProduct(models.Model):
    """商城首页商品导购商品"""
    class Meta:
        db_table = "shoppingguide_product"

    parentId = models.IntegerField() # 导购商品归属子栏目id
    productId = models.IntegerField() # 商品id
    addTime = models.DateTimeField(auto_now_add=True) # 添加时间
    addAdminId = models.IntegerField() # 添加导购商品管理员id
    show = models.BooleanField(default = True) # 商品是否展示
    order = models.IntegerField(default = 1) # 商品展示顺序（数字越大，展示越前）






