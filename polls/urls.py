from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    # Examples:
    url(r'^home$', 'home_page', name='home'),
    url(r'^question$', 'answer_question', name="question"),
    url(r'^result$', 'get_result', name="result"),
)
