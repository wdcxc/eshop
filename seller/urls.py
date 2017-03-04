from django.conf.urls import url

from seller.views.common import CommonView

app_name = "seller"

# common
urlpatterns = [
    url(r'^common/login$',CommonView.as_view(),name="login"),
]