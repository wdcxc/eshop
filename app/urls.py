from django.conf.urls import url

from app.views.common import CommonView

app_name = "app"

# common
urlpatterns = [
    url(r'^common/index$',CommonView.as_view(), name = "index"),
    url(r'^common/introduction$',CommonView.as_view(), name = "introduction"),
    url(r'^common/order$',CommonView.as_view(), name = "order"),
    url(r'^common/search$',CommonView.as_view(), name = "search"),
    url(r'^common/shopcart$',CommonView.as_view(), name = "shopcart"),
    url(r'^common/success$',CommonView.as_view(), name = "success"),
    url(r'^common/activity$',CommonView.as_view(), name = "activity"),
    url(r'^common/fail$',CommonView.as_view(), name = "fail"),
]
