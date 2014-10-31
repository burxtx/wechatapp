from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^wechatapp/polls/', include('polls.urls', namespace='polls')),
    url(r'^wechatapp/admin/', include(admin.site.urls)),
)
