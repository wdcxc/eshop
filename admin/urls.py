from django.conf.urls import url

from admin.views.adminadmin import AdminAdminView
from admin.views.appadmin import AppAdminView
from admin.views.common import CommonView
from admin.views.customeradmin import CustomerAdminView
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

# adminadmin
urlpatterns += [
    url(r'^adminadmin/index$',AdminAdminView.as_view(),name="adminAdminIndex"),
    url(r'^adminadmin/addAdmin',AdminAdminView.as_view(),name="addAdmin"),
    url(r'^adminadmin/deleteAdmin',AdminAdminView.as_view(),name="deleteAdmin"),
]

# customeradmin
urlpatterns += [
    url(r'^customeradmin/index$',CustomerAdminView.as_view(),name="customerAdminIndex"),
]

# seller
urlpatterns += [
    url(r'^selleradmin/index$',SellerAdminView.as_view(),name="sellerAdminIndex"),
]

# appadmin
urlpatterns += [
    url(r'^appadmin/index$',AppAdminView.as_view(),name="appAdminIndex"),
    url(r'appadmin/carousel$',AppAdminView.as_view(),name="appAdminCarousel"),
    url(r'appadmin/addCarousel$',AppAdminView.as_view(),name="appAdminAddCarousel"),
    url(r'appadmin/updateCarousel$',AppAdminView.as_view(),name="appAdminUpdateCarousel"),
    url(r'appadmin/deleteCarousel$',AppAdminView.as_view(),name="appAdminDeleteCarousel"),
]