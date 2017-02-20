from django.conf.urls import url
from . import views

app_name = "customer"
urlpatterns = [
    url(r'^login$', views.login, name="login"),
    url(r'^doLogin', views.doLogin, name="doLogin"),
    url(r'^register', views.register, name="register"),
    url(r'^forgetpwd', views.forgetPwd, name="forgetPwd"),
    url(r'^captcha/(?P<action>\w+)$', views.captcha, name="captcha"),
]