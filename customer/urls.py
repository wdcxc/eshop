from django.conf.urls import url

from customer.views.collection import CollectionView
from customer.views.common import CommonView
from customer.views.information import InformationView
from customer.views.order import OrderView
from customer.views.service import ServiceView

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
    url(r'^common/bill', CommonView.as_view(), name="bill"),
    url(r'^common/refundapply', CommonView.as_view(), name="refundapply"),
    url(r'.*/logout$', CommonView.as_view(), name="logout"),  # 登出账号
]

# 买家信息
urlpatterns += [
    url(r'^information/index$', InformationView.as_view(), name="index"),  # 买家首页
    url(r'^information/information$', InformationView.as_view(), name="information"),  # 买家个人信息
    url(r'^information/address$', InformationView.as_view(), name="address"),  # 收货地址
    url(r'^information/addAddress$', InformationView.as_view(), name="addAddress"),  # 新增收货地址
    url(r'^information/deleteAddress$', InformationView.as_view(), name="deleteAddress"),  # 删除收货地址
    url(r'^information/updateAddress$', InformationView.as_view(), name="updateAddress"),  # 修改收货地址
    url(r'^information/setDefaultAddr', InformationView.as_view(), name="setDefaultAddr"),  # 设置默认收货地址
    url(r'^information/uploadAvatar', InformationView.as_view(), name="uploadAvatar"),  # 上传头像
    url(r'^information/citys', InformationView.as_view(), name="citys"),  # 城市列表
    url(r'^information/dists', InformationView.as_view(), name="dists"),  # 区列表
]

# 订单
urlpatterns += [
    url(r'^order/order$', OrderView.as_view(), name="order"),  # 待发货订单
    url(r'^order/receiveorder$', OrderView.as_view(), name="receiveorder"),  # 待收货订单
    url(r'^order/evaluateorder$', OrderView.as_view(), name="evaluateorder"),  # 待评价订单
    url(r'^order/refund$', OrderView.as_view(), name="refund"),  # 订单退款
    url(r'^order/receiveProduct$', OrderView.as_view(), name="receiveProduct"),  # 收货
    url(r'^order/goodsevaluate', OrderView.as_view(), name="goodsevaluate"), # 订单评价
]

# 收藏
urlpatterns += [
    url(r'^collection/collection$', CollectionView.as_view(), name="collection"),
]

# 服务
urlpatterns += [
    url(r'^service/suggestion$', ServiceView.as_view(), name="suggestion"),  # 添加意见
    url(r'^service/addSuggestion$', ServiceView.as_view(), name="addSuggestion"),  # 添加意见
    url(r'^service/message$', ServiceView.as_view(), name="message"),  # 咨询信息
    url(r'^service/consult$', ServiceView.as_view(), name="consult"),  # 商品咨询
    url(r'^service/suggestionMessage$', ServiceView.as_view(), name="suggestionMessage"),  # 意见信息
    url(r'^service/refundMessage$', ServiceView.as_view(), name="refundMessage"),  # 退款信息
]
