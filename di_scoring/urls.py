from django.conf.urls import patterns, include, url
from di_scoring import views

urlpatterns = patterns('',
    url(r'^$', views.indexView, name='index'),
    # url(r'login/$', 'django.contrib.auth.views.login',
    #     {'template_name': 'admin/login.html'},
    #     name='login',
    # ),
    # url(r'logout/', 'django.contrib.auth.views.logout', name='logout'),
)
