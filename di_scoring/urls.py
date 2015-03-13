from django.conf.urls import patterns, include, url
from django.contrib import admin
from di_scoring import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/$', 'django.contrib.auth.views.login',
        {'template_name': 'admin/login.html'},
        name='login',
    ),
    url(r'logout/', 'django.contrib.auth.views.logout', name='logout'),
)
