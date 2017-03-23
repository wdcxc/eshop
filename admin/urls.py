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
    url(r'^common/doLogin$',CommonView.as_view(),name="doLogin"),
    url(r'^common/logout$',CommonView.as_view(),name="logout"),
    url(r'^common/index$', CommonView.as_view(), name="index"),
    url(r'^common/generateCaptcha/[0-9\.]*$', CommonView.as_view(), name="generateCaptcha"),
    url(r'^common/valifyCaptcha$', CommonView.as_view(), name="valifyCaptcha")
]

# adminadmin 管理员管理
urlpatterns += [
    url(r'^adminadmin/index$',AdminAdminView.as_view(),name="adminAdminIndex"),
    url(r'^adminadmin/addAdmin$',AdminAdminView.as_view(),name="addAdmin"),
    url(r'^adminadmin/deleteAdmin$',AdminAdminView.as_view(),name="deleteAdmin"),
]

# customeradmin 顾客管理
urlpatterns += [
    url(r'^customeradmin/index$',CustomerAdminView.as_view(),name="customerAdminIndex"),
]

# seller 商家管理
urlpatterns += [
    url(r'^selleradmin/index$',SellerAdminView.as_view(),name="sellerAdminIndex"),
]

# appadmin 商城管理
urlpatterns += [
    url(r'^appadmin/index$',AppAdminView.as_view(),name="appAdminIndex"),
    url(r'^appadmin/carousel$',AppAdminView.as_view(),name="appAdminCarousel"),# 轮播图管理
    url(r'^appadmin/addCarousel$',AppAdminView.as_view(),name="appAdminAddCarousel"),
    url(r'^appadmin/updateCarousel$',AppAdminView.as_view(),name="appAdminUpdateCarousel"),
    url(r'^appadmin/deleteCarousel$',AppAdminView.as_view(),name="appAdminDeleteCarousel"),
    url(r'^appadmin/uploadCarouselImg$',AppAdminView.as_view(),name="appAdminUploadCarouselImg"),
    url(r'^appadmin/updateCarouselImg$',AppAdminView.as_view(),name="appAdminUpdateCarouselImg"),
    url(r'^appadmin/productCategory$',AppAdminView.as_view(),name="appAdminProductCategory"), # 商品目录导航管理
    url(r'^appadmin/activity$',AppAdminView.as_view(),name="appAdminActivity"), # 商城活动
]

# productadmin 商品管理
urlpatterns += [
    url(r'^productadmin/index$',ProductAdminView.as_view(),name="productAdminIndex"),
    url(r'^productadmin/product$',ProductAdminView.as_view(),name="productAdminProduct"), # 商品管理
    url(r'^productadmin/category$',ProductAdminView.as_view(),name="productAdminCategory"), # 商品类别管理
    url(r'^productadmin/addCategory$', ProductAdminView.as_view(), name="productAdminAddCategory"),
    url(r'^productadmin/updateCategory$',ProductAdminView.as_view(),name="productAdminUpdateCategory"),
    url(r'^productadmin/deleteCategory$',ProductAdminView.as_view(),name="productAdminDeleteCategory"),
    url(r'^productadmin/tag$',ProductAdminView.as_view(),name="productAdminTag"), # 商品标签管理
]