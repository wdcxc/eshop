from django.conf.urls import url

from .views import AppView

app_name = "app"
urlpatterns = [
    url(r'^index$',AppView.as_view(), name = "index"),
]
