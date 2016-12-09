from django.conf.urls import url

from . import views
from views import GetTweets, GetUserInfo

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^latest_tweets/(.+)$', GetTweets()),
    url(r'^user_info/(.+)$', GetUserInfo()),
]
