from django.conf.urls import url
from . import views

#url patterns dict must contain an item for EACH ROUTE!!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show)
]
