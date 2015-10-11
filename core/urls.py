from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^farm_group/(?P<farm_group_id>[0-9]+)/$', views.farm_group, name='farm_group'),
    url(r'^farm_group/(?P<farm_group_id>[0-9]+)/export/$', views.farm_group_export, name='farm_group_export'),
    url(r'^farm_group/(?P<farm_group_id>[0-9]+)/farm_event/$', views.farm_event, name='farm_event'),
    url(r'^farm_group/(?P<farm_group_id>[0-9]+)/farm_event/(?P<farm_event_id>[0-9]+)/$', views.farm_event, name='farm_event')
]