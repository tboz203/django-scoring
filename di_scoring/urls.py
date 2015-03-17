from django.conf.urls import patterns, include, url
from di_scoring import views

urlpatterns = patterns('',
    url(r'^$', views.indexView, name='index'),
    url(r'^teams/$', views.TeamListView.as_view(), name='team_list'),
    url(r'^teams/(?P<slug>[\w\ ]+)/$', views.TeamDetailView.as_view(), name='team_detail'),
)
