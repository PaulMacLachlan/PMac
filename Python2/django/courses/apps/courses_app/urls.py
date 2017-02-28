
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create_course),
    # url(r'^confirm_delete$', views.confirm_delete),
    # url(r'^no_delete$', views.no_delete),
    # url(r'^yes_delete$', views.yes_delete),
    url(r'^$', views.index),
    # url(r'^courses/destroy/(?P<id>\d+)$', views.destroy)
]
