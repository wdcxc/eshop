from django.conf.urls import url

from customer.views.common import CommonView

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
    url(r'^common/index$', CommonView.as_view(), name="index"),
    url(r'^common/information$', CommonView.as_view(), name="information"),
    url(r'^common/address$', CommonView.as_view(), name="address"),
    url(r'^common/order$', CommonView.as_view(), name="order"),
    url(r'^common/evaluate$', CommonView.as_view(), name="evaluate"),
]
