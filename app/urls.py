from django.conf.urls import url

from app.views.common import CommonView

app_name = "app"

# common
urlpatterns = [
    url(r'^common/login$',CommonView.as_view(), name = "login"),
    url(r'^common/index',CommonView.as_view(), name = "index"),
]