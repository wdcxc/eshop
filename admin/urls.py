from django.conf.urls import url

from admin.views.admin import AdminView
from admin.views.common import CommonView
from admin.views.customer import CustomerView
from admin.views.seller import SellerView

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

# admin
urlpatterns += [
    url(r'^admin/index$',AdminView.as_view(),name="adminIndex"),
    url(r'^admin/addAdmin',AdminView.as_view(),name="addAdmin"),
    url(r'^admin/deleteAdmin',AdminView.as_view(),name="deleteAdmin"),
]

# customer
urlpatterns += [
    url(r'^customer/index$',CustomerView.as_view(),name="customerIndex"),
]

# seller
urlpatterns += [
    url(r'^seller/index$',SellerView.as_view(),name="sellerIndex"),
]