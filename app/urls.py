from django.conf.urls import url

from .views import BaseView

app_name = "app"
urlpatterns = [
    url(r'^index$',BaseView.as_view(),name="index"),
]


