from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # there's probably a better way to do this.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('di_scoring.urls', namespace='di_scoring')),
)
