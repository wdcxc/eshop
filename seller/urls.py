from django.conf.urls import url

from .views import SellerView

app_name = "seller"
urlpatterns = [
    url(r'^login$',SellerView.as_view(),name="login"),
]