from __future__ import unicode_literals

from django.db import models


class NodeModel(models.Model):
    """节点模型"""
    name = models.CharField(max_length=30)  # 节点名称
    controller = models.CharField(max_length=30)  # 节点归属controller
    action = models.CharField(max_length=30)  # 节点归属action
    linkUrl = models.URLField()  # 节点链接
    addTime = models.DateTimeField(auto_now_add=True)  # 添加时间
    addAdminId = models.IntegerField(default=0)  # 添加管理员id，0:超级管理员

    class Meta:
        db_table = "admin_node"


class GroupModel(models.Model):
    """管理权限组模型"""
    name = models.CharField(max_length=30)  # 权限组名称
    addTime = models.DateTimeField(auto_now_add=True)  # 添加时间
    addAdminId = models.IntegerField(default=0)  # 添加管理员id，0:超级管理员
    nodes = models.ManyToManyField(NodeModel,related_name="nodes")  # 拥有节点

    class Meta:
        db_table = "admin_group"


class AdminModel(models.Model):
    """管理员模型"""
    username = models.CharField(max_length=30, unique=True)  # 用户名
    password = models.CharField(max_length=200)  # 密码
    loginTime = models.DateTimeField()  # 账户最近登录时间
    root = models.BooleanField(default=False)  # 是否是超级管理员
    addTime = models.DateTimeField(auto_now_add=True)  # 添加时间
    addAdminId = models.IntegerField(default=0)  # 添加管理员id，0:超级管理员
    groups = models.ManyToManyField(GroupModel,related_name="groups")  # 拥有权限组

    class Meta:
        db_table = "admin"
