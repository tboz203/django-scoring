from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # there's probably a better way to do this.
    url(r'^', include('di_scoring.urls', namespace='di_scoring')),
)
