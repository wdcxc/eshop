from django.conf.urls import url

from app.views.common import CommonView
from app.views.order import OrderView

app_name = "app"

# common
urlpatterns = [
    url(r'^common/index$', CommonView.as_view(), name="index"),
    url(r'^common/introduction$', CommonView.as_view(), name="introduction"),
    url(r'^common/search$', CommonView.as_view(), name="search"),
    url(r'^common/shopcart$', CommonView.as_view(), name="shopcart"),
    url(r'^common/deleteShopcart$', CommonView.as_view(), name="deleteShopcart"),
    url(r'^common/addShopcart$', CommonView.as_view(), name="addShopcart"),
    url(r'^common/buynow$', CommonView.as_view(), name="buynow"),
    url(r'^common/activity$', CommonView.as_view(), name="activity"),
    url(r'^common/contact$', CommonView.as_view(), name="contact"),
    url(r'^common/about', CommonView.as_view(), name="about"),
    url(r'^common/help', CommonView.as_view(), name="help"),
    url(r'.*/logout$', CommonView.as_view(), name="logout"),
    url(r'^common/addCollection',CommonView.as_view(),name="addCollection"),
    url(r'^common/deleteCollection',CommonView.as_view(),name="deleteCollection"),
]

# 订单
urlpatterns += [
    url(r'^order/success$', OrderView.as_view(), name="success"),
    url(r'^order/fail$', OrderView.as_view(), name="fail"),
    url(r'^order/order$', OrderView.as_view(), name="order"),
    url(r'^order/addOrder$', OrderView.as_view(), name="addOrder"),
    url(r'^order/payOrder$', OrderView.as_view(), name="payOrder"),
    url(r'^order/cancelOrder$', OrderView.as_view(), name="cacelOrder"),
]
