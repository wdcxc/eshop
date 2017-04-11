from django.conf.urls import url

from admin.views.adminadmin import AdminAdminView
from admin.views.appadmin import AppAdminView
from admin.views.common import CommonView
from admin.views.customeradmin import CustomerAdminView
from admin.views.productadmin import ProductAdminView
from admin.views.selleradmin import SellerAdminView

app_name = "admin"

# common
urlpatterns = [
    url(r'^common/login$', CommonView.as_view(), name="login"),
    url(r'^common/doLogin$', CommonView.as_view(), name="doLogin"),
    url(r'^common/logout$', CommonView.as_view(), name="logout"),
    url(r'^common/index$', CommonView.as_view(), name="index"),
    url(r'^common/generateCaptcha/[0-9\.]*$', CommonView.as_view(), name="generateCaptcha"),
    url(r'^common/valifyCaptcha$', CommonView.as_view(), name="valifyCaptcha"),
    url(r'^common/forbidden$',CommonView.as_view(),name="forbidden"),
]

# adminadmin 管理员管理
urlpatterns += [
    url(r'^adminadmin/adminIndex$', AdminAdminView.as_view(), name="adminAdminAdminIndex"),  # 管理员管理
    url(r'^adminadmin/addAdmin$', AdminAdminView.as_view(), name="adminAdminAddAdmin"),
    url(r'^adminadmin/deleteAdmin$', AdminAdminView.as_view(), name="adminAdminDeleteAdmin"),
    url(r'^adminadmin/updateAdmin$', AdminAdminView.as_view(), name="adminAdminUpdateAdmin"),
    url(r'^adminadmin/groupIndex$', AdminAdminView.as_view(), name="adminAdminGroupIndex"),  # 权限组管理
    url(r'^adminadmin/addGroup$', AdminAdminView.as_view(), name="adminAdminAddGroup"),
    url(r'^adminadmin/deleteGroup$', AdminAdminView.as_view(), name="adminAdminDeleteGroup"),
    url(r'^adminadmin/updateGroup$', AdminAdminView.as_view(), name="adminAdminUpdateGroup"),
    url(r'^adminadmin/nodeIndex$', AdminAdminView.as_view(), name="adminAdminNodeIndex"),  # 节点管理
    url(r'^adminadmin/addNode$', AdminAdminView.as_view(), name="adminAdminAddNode"),
    url(r'^adminadmin/deleteNode$', AdminAdminView.as_view(), name="adminAdminDeleteNode"),
    url(r'^adminadmin/updateNode$', AdminAdminView.as_view(), name="adminAdminUpdateNode"),
    url(r'^adminadmin/setting$', AdminAdminView.as_view(), name="adminAdminSetting"),
]

# customeradmin 买家管理
urlpatterns += [
    url(r'^customeradmin/index$', CustomerAdminView.as_view(), name="customerAdminIndex"),
    url(r'^customeradmin/lockAccount$', CustomerAdminView.as_view(), name="lockCustomer"),
    url(r'^customeradmin/unlockAccount$', CustomerAdminView.as_view(), name="unlockCustomer"),
]

# seller 卖家管理
urlpatterns += [
    url(r'^selleradmin/index$', SellerAdminView.as_view(), name="sellerAdminIndex"),
    url(r'^selleradmin/lockAccount$', SellerAdminView.as_view(), name="lockSeller"),
    url(r'^selleradmin/unlockAccount$', SellerAdminView.as_view(), name="unlockSeller"),
]

# appadmin 商城管理
urlpatterns += [
    url(r'^appadmin/index$', AppAdminView.as_view(), name="appAdminIndex"),
    url(r'^appadmin/carousel$', AppAdminView.as_view(), name="appAdminCarousel"),  # 轮播图管理
    url(r'^appadmin/addCarousel$', AppAdminView.as_view(), name="appAdminAddCarousel"),
    url(r'^appadmin/updateCarousel$', AppAdminView.as_view(), name="appAdminUpdateCarousel"),
    url(r'^appadmin/deleteCarousel$', AppAdminView.as_view(), name="appAdminDeleteCarousel"),
    url(r'^appadmin/uploadCarouselImg$', AppAdminView.as_view(), name="appAdminUploadCarouselImg"),
    url(r'^appadmin/updateCarouselImg$', AppAdminView.as_view(), name="appAdminUpdateCarouselImg"),
    url(r'^appadmin/productCategory$', AppAdminView.as_view(), name="appAdminProductCategory"),  # 商品目录导航管理
    url(r'^appadmin/shoppingGuide$', AppAdminView.as_view(), name="appAdminShoppingGuide"),  # 商城首页商品导购管理
    url(r'^appadmin/addShoppingGuideChannel$', AppAdminView.as_view(), name="appAdminAddShoppingGuideChannel"),
    url(r'^appadmin/updateShoppingGuideChannel$', AppAdminView.as_view(), name="appAdminUpdateShoppingGuideChannel"),
    url(r'^appadmin/deleteShoppingGuideChannel$', AppAdminView.as_view(), name="appAdminDeleteShoppingGuideChannel"),
    url(r'^appadmin/addShoppingGuideSubchannel$', AppAdminView.as_view(), name="appAdminAddShoppingGuideSubchannel"),
    url(r'^appadmin/updateShoppingGuideSubchannel$', AppAdminView.as_view(),
        name="appAdminUpdateShoppingGuideSubchannel"),
    url(r'^appadmin/deleteShoppingGuideSubchannel$', AppAdminView.as_view(),
        name="appAdminDeleteShoppingGuideSubchannel"),
    url(r'^appadmin/addShoppingGuideProduct$', AppAdminView.as_view(), name="appAdminAddShoppingGuideProduct"),
    url(r'^appadmin/updateShoppingGuideProduct$', AppAdminView.as_view(), name="appAdminUpdateShoppingGuideProduct"),
    url(r'^appadmin/deleteShoppingGuideProduct$', AppAdminView.as_view(), name="appAdminDeleteShoppingGuideProduct"),
    url(r'^appadmin/uploadShoppingGuideProductImg$', AppAdminView.as_view(),
        name="appAdminUploadShoppingGuideProductImg"),
    url(r'^appadmin/updateShoppingGuideProductImg$', AppAdminView.as_view(),
        name="appAdminUpdateShoppingGuideProductImg"),
]

# productadmin 商品管理
urlpatterns += [
    url(r'^productadmin/index$', ProductAdminView.as_view(), name="productAdminIndex"),
    url(r'^productadmin/product$', ProductAdminView.as_view(), name="productAdminProduct"),  # 商品管理
    url(r'^productadmin/category$', ProductAdminView.as_view(), name="productAdminCategory"),  # 商品类别管理
    url(r'^productadmin/addCategory$', ProductAdminView.as_view(), name="productAdminAddCategory"),
    url(r'^productadmin/updateCategory$', ProductAdminView.as_view(), name="productAdminUpdateCategory"),
    url(r'^productadmin/deleteCategory$', ProductAdminView.as_view(), name="productAdminDeleteCategory"),
    url(r'^productadmin/property$', ProductAdminView.as_view(), name="productAdminProperty"),  # 商品属性管理
    url(r'^productadmin/addProperty$', ProductAdminView.as_view(), name="productAdminAddProperty"),
    url(r'^productadmin/updateProperty$', ProductAdminView.as_view(), name="productAdminUpdateProperty"),
    url(r'^productadmin/deleteProperty$', ProductAdminView.as_view(), name="productAdminDeleteProperty"),
]
