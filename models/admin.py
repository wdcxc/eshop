from __future__ import unicode_literals

from django.db import models

class AdminModel(models.Model):
    class Meta:
        db_table = "admin"

    username = models.CharField(max_length=30,unique=True) # 用户名
    password = models.CharField(max_length=130) # 密码
    loginTime = models.DateTimeField() # 账户最近登录时间
    grade = models.IntegerField(default=999) # 用户等级（数字越高，等级越低）