from django.conf.urls import url

from . import views

app_name = "admin"
urlpatterns = [
    url(r'^login$',views.login,name="login"),
    url(r'^getCaptchaImage/[0-9\.]*$',views.getCaptchaImage,name="getCaptchaImage")
]