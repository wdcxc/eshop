from django.conf.urls import url

from .views import CustomerView

app_name = "customer"
urlpatterns = [
    url(r'^login$', CustomerView.as_view(), name="login"),
    url(r'^doLogin$', CustomerView.as_view(), name="doLogin"),
    url(r'^register$', CustomerView.as_view(), name="register"),
    url(r'^doRegister$', CustomerView.as_view(), name="doRegister"),
    url(r'^forgetpwd$', CustomerView.as_view(), name="forgetPwd"),
    url(r'^getCaptchaImage/[0-9\.]*$', CustomerView.as_view(), name="getCaptchaImage"),
    url(r'^valifyCaptcha$', CustomerView.as_view(), name="valifyCaptcha"),
]
