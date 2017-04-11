from django.conf.urls import url

from seller.views.common import CommonView
from seller.views.goods import GoodView
from seller.views.order import OrderView

app_name = "seller"

# common
urlpatterns = [
    url(r'^common/doLogin$', CommonView.as_view(), name="doLogin"),
    url(r'^common/register$', CommonView.as_view(), name="register"),
    url(r'^common/doRegister$', CommonView.as_view(), name="doRegister"),
    url(r'^common/forgetpwd$', CommonView.as_view(), name="forgetPwd"),
    url(r'^common/generateCaptcha/[0-9\.]*$', CommonView.as_view(), name="generateCaptcha"),
    url(r'^common/valifyCaptcha$', CommonView.as_view(), name="valifyCaptcha"),
    url(r'^common/index$', CommonView.as_view(), name="index"),
    url(r'^common/login$', CommonView.as_view(), name="login"),
    url(r'^common/consult$', CommonView.as_view(), name="consult"),
    url(r'^common/opinion$', CommonView.as_view(), name="opinion"),
    url(r'^common/personalinfo$', CommonView.as_view(), name="personalinfo"),
    url(r'^common/shopinfo$', CommonView.as_view(), name="shopinfo"),
    url(r'^common/uploadThumbnail$', CommonView.as_view(), name="uploadThumbnail"),
]

# 商品
urlpatterns += [
    url(r'^goods/goodslist', GoodView.as_view(), name="goodslist"),
    url(r'^goods/addGoods$', GoodView.as_view(), name="addGoods"),
    url(r'^goods/updateGoods$', GoodView.as_view(), name="updateGoods"),
    url(r'^goods/deleteGoods$', GoodView.as_view(), name="deleteGoods"),
    url(r'^goods/updateStatus$', GoodView.as_view(), name="updateStatus"),
    url(r'^goods/uploadImage$',GoodView.as_view(),name="uploadImage"),
    url(r'^goods/deleteImage$',GoodView.as_view(),name="deleteImage"),
    url(r'^goods/getSubCategories$',GoodView.as_view(),name="getSubCategories"),
]

# 订单
urlpatterns += [
    url(r'^order/order$', OrderView.as_view(), name="order"),
    url(r'^order/receiveorder$', OrderView.as_view(), name="receiveorder"),
    url(r'^order/evaluateorder$', OrderView.as_view(), name="evaluateorder"),
    url(r'^order/sendProduct$', OrderView.as_view(), name="sendProduct"),
    url(r'^order/refund$', OrderView.as_view(), name="refund"),
]