from django.conf.urls import patterns, include, url
import django.contrib.auth.views as authviews
from di_scoring import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'login/$', 'django.contrib.auth.views.login',
            {'template_name': 'admin/login.html'},
            name='login',
        ),
        url(r'logout/$', authviews.logout, name='logout'),
)
