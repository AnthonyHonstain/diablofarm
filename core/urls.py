from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^farm_group/(?P<farm_group_id>[0-9]+)/$', views.farm_group, name='farm_group')
]