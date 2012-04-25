from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url('', 'hitcount.views.hit', name='hit'),
)
