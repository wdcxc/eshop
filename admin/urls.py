from django.conf.urls import url

from .views import AdminView

app_name = "admin"
urlpatterns = [
    url(r'^login$', AdminView.as_view(), name="login"),
    url(r'^index$', AdminView.as_view(), name="index"),
    url(r'^customer$', AdminView.as_view(), name="customer"),
    url(r'^seller$', AdminView.as_view(), name="seller"),
    url(r'^admin$', AdminView.as_view(), name="admin"),
    url(r'^statistic$', AdminView.as_view(), name="statistic"),
    url(r'^getCaptchaImage/[0-9\.]*$', AdminView.as_view(), name="getCaptchaImage"),
    url(r'^valifyCaptcha$', AdminView.as_view(), name="valifyCaptcha")
]
