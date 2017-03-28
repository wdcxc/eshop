import hashlib

from admin.views.adminbaseview import AdminBaseView
from models.admin import AdminModel, GroupModel, NodeModel
from util.baseview import loginRequire


class AdminAdminView(AdminBaseView):
    @loginRequire()
    def adminIndex(self, request):
        """管理员管理首页"""
        admins = AdminModel.objects.all()
        for admin in admins:
            admin.__dict__.update({"groups":admin.groups.all()})
        self.context["admins"] = [admin.__dict__ for admin in admins]

    @loginRequire()
    def addAdmin(self, request):
        """添加管理员"""
        if request.method == "GET":
            groups = GroupModel.objects.all()
            self.context["groups"] = groups
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            vals = {
                "username":request.POST.get("username"),
                "password":hashlib.sha512(request.POST.get("password").encode("utf8")).hexdigest(),
                "root":request.POST.get("root"),
                "groupIds":request.POST.getlist("groupIds[]"),
                "addAdminId":request.session["user"]["id"],
            }
            groups = GroupModel.objects.filter(id__in=vals["groupIds"])
            del vals["groupIds"]
            admin = AdminModel(**vals)
            admin.save()
            admin.groups.add(*groups)
            self.context = {"code":200,"msg":"添加管理员成功","data":{"id":admin.id}}

    @loginRequire()
    def updateAdmin(self, request):
        if request.method == "GET":
            admin = AdminModel.objects.get(id=request.GET.get("id"))
            groups = GroupModel.objects.all()
            groupIds = ','.join([str(group["id"]) for group in admin.groups.all().values()])
            admin.__dict__.update({"groupIds":groupIds,"groups":groups})
            self.context["admin"] = admin.__dict__
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            admin = AdminModel.objects.get(id=request.POST.get("id"))
            admin.root = request.POST.get("root")
            if request.POST.get("password"):
                print(request.POST.get("password"))
                admin.password = hashlib.sha512(request.POST.get("password").encode("utf-8")).hexdigest()
            groups = GroupModel.objects.filter(id__in=request.POST.getlist("groupIds[]"))
            admin.groups.set(groups)
            admin.save()
            self.context = {"code": 200, "msg": "修改管理员成功", "data": {"id": admin.id}}

    @loginRequire()
    def deleteAdmin(self, request):
        """删除管理员"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        adminId = request.POST.get("id")
        AdminModel.objects.get(id=adminId).delete()
        self.context = {"code":200,"msg":"删除管理员成功","data":{"id":adminId}}

    @loginRequire()
    def groupIndex(self, request):
        """权限组管理首页"""
        groups = GroupModel.objects.all()
        for group in groups:
            group.__dict__.update({"nodes":group.nodes.all()})
        self.context["groups"] = [g.__dict__ for g in groups]

    @loginRequire()
    def addGroup(self, request):
        """添加新权限组"""
        if request.method == "GET":
            self.context["nodes"] = NodeModel.objects.all().order_by("controller","action")
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            vals = {
                "name":request.POST.get("name"),
                "addAdminId":request.session["user"]["id"],
                "nodeIds":request.POST.getlist("nodeIds[]")
            }
            nodes = NodeModel.objects.filter(id__in=vals["nodeIds"])
            del vals["nodeIds"]
            group = GroupModel(**vals)
            group.save()
            group.nodes.add(*nodes)
            self.context = {"code":200,"msg":"添加新权限组成功","data":{"id":group.id}}

    @loginRequire()
    def deleteGroup(self, request):
        """删除权限组"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        groupId = request.POST.get("id")
        GroupModel.objects.get(id=groupId).delete()
        self.context = {"code":200,"msg":"删除权限组成功","data":{"id":groupId}}

    @loginRequire()
    def updateGroup(self, request):
        """修改权限组"""
        if request.method == "GET":
            group = GroupModel.objects.get(id=request.GET.get("id"))
            nodes = NodeModel.objects.all()
            group.__dict__.update({"nodeIds":",".join([str(node["id"]) for node in group.nodes.all().values()]),"nodes":nodes})
            self.context["group"] = group.__dict__
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            group = GroupModel.objects.get(id=request.POST.get("id"))
            group.name = request.POST.get("name")
            group.save()
            nodes = NodeModel.objects.filter(id__in=request.POST.getlist("nodeIds[]"))
            group.nodes.set(nodes)
            print(request.POST)
            self.context = {"code":200,"msg":"修改权限组成功","data":{"id":group.id}}

    @loginRequire()
    def nodeIndex(self, request):
        """节点管理首页"""
        self.context["nodes"] = NodeModel.objects.all()

    @loginRequire()
    def addNode(self, request):
        """添加节点"""
        if request.method == "GET":
            pass
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("name", "controller", "action", "linkUrl")
            vals = {}
            for key in keys:
                vals[key] = request.POST.get(key)
            vals["addAdminId"] = request.session["user"]["id"]
            node, created = NodeModel.objects.get_or_create({}, **vals)
            if created:
                self.context = {"code": 200, "msg": "添加节点成功", "data": {"id": node.id}}
            else:
                self.context = {"code": 4, "msg": "节点已存在", "data": {"id": node.id}}

    @loginRequire()
    def deleteNode(self, request):
        """删除节点"""
        self.response_["type"] = self.RESPONSE_TYPE_JSON
        nodeId = request.POST.get("id")
        NodeModel.objects.get(id=nodeId).delete()
        self.context = {"code": 200, "msg": "删除节点成功", "data": {"id": nodeId}}

    @loginRequire()
    def updateNode(self, request):
        if request.method == "GET":
            self.context["node"] = NodeModel.objects.get(id=request.GET.get("id"))
        elif request.method == "POST":
            self.response_["type"] = self.RESPONSE_TYPE_JSON
            keys = ("name","controller","action","linkUrl")
            vals = {}
            for key in keys:
                vals[key] = request.POST.get(key)
            nodeId = request.POST.get("id")
            NodeModel.objects.filter(id=nodeId).update(**vals)
            self.context = {"code":200,"msg":"修改节点成功","data":{"id":nodeId}}