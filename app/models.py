from __future__ import unicode_literals

from django.db import models

class CarouselModel(models.Model):
    """首页轮播页"""

    class Meta():
        db_table = "index_carousel"

    title = models.CharField(max_length=50) # 标题
    show = models.BooleanField(default=False) # 是否显示
    order = models.IntegerField(default=1) # 展示权重（权重越大，展示越前）
    imgUrl = models.URLField() # 图片链接地址
    linkUrl = models.URLField() # 点击跳转链接
    addTime = models.DateTimeField(auto_now_add=True)

