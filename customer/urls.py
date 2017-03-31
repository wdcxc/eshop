from django.conf.urls import url

from customer.views.common import CommonView
from customer.views.information import InformationView
from customer.views.order import OrderView
app_name = "customer"

# common
urlpatterns = [
    url(r'^common/login$', CommonView.as_view(), name="login"),
    url(r'^common/doLogin$', CommonView.as_view(), name="doLogin"),
    url(r'^common/register$', CommonView.as_view(), name="register"),
    url(r'^common/doRegister$', CommonView.as_view(), name="doRegister"),
    url(r'^common/forgetpwd$', CommonView.as_view(), name="forgetPwd"),
    url(r'^common/generateCaptcha/[0-9\.]*$', CommonView.as_view(), name="generateCaptcha"),
    url(r'^common/valifyCaptcha$', CommonView.as_view(), name="valifyCaptcha"),
    url(r'^common/evaluate$', CommonView.as_view(), name="evaluate"),
    url(r'^common/collection', CommonView.as_view(), name="collection"),
    url(r'^common/consult', CommonView.as_view(), name="consult"),
    url(r'^common/opinion', CommonView.as_view(), name="opinion"),
    url(r'^common/message', CommonView.as_view(), name="message"),
    url(r'^common/bill', CommonView.as_view(), name="bill"),
    url(r'^common/refundapply', CommonView.as_view(), name="refundapply"),
    url(r'^common/goodsevaluate', CommonView.as_view(), name="goodsevaluate"),
]

# 买家信息
urlpatterns += [
    url(r'^information/index$', InformationView.as_view(), name="index"), # 买家首页
    url(r'^information/information$', InformationView.as_view(), name="information"), # 买家个人信息
    url(r'^information/address$', InformationView.as_view(), name="address"), # 收货地址
    url(r'^information/addAddress$', InformationView.as_view(), name="address"), # 新增收货地址
    url(r'^information/uploadAvatar', InformationView.as_view(), name="uploadAvatar"), # 上传头像
    url(r'^information/citys', InformationView.as_view(), name="citys"),  # 城市列表
    url(r'^information/dists', InformationView.as_view(), name="dists"),  # 区列表
]

# 订单
urlpatterns += [
    url(r'^order/order$',OrderView.as_view(),name="order"), # 订单
]
