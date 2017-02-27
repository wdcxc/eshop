from django.conf.urls import url

from . import views

app_name = "customer"
urlpatterns = [
    url(r'^login$', views.login, name="login"),
    url(r'^doLogin$', views.doLogin, name="doLogin"),
    url(r'^register$', views.register, name="register"),
    url(r'^doRegister$',views.doRegister,name="doRegister"),
    url(r'^forgetpwd$', views.forgetPwd, name="forgetPwd"),
    url(r'^captcha/[0-9\.]*$', views.captcha, name="captcha"),
    url(r'^valifyCaptcha$', views.valifyCaptcha, name="valifyCaptcha"),
]
