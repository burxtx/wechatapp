from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    # Examples:
    url(r'^home$', 'home_page', name='home'),
    # url(r'^question/(\d+)$', '', name="question"),
    # url(r'^result/(\d+)$', '', name="result"),
)
