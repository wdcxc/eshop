from django.conf.urls import url

from seller.views.common import CommonView

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
    url(r'^common/login', CommonView.as_view(), name="login"),
    url(r'^common/consult', CommonView.as_view(), name="consult"),
    url(r'^common/opinion', CommonView.as_view(), name="opinion"),
    url(r'^common/verify', CommonView.as_view(), name="verify"),
]