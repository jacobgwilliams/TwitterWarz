from . import views
from views import GetTweets, GetUserInfo
from django.conf.urls import url
from twitterwarz import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^latest_tweets/(.+)$', GetTweets()),
    url(r'^user_info/(.+)$', GetUserInfo()),
    url(r'^test/$', views.test, name='test'),
    url(r'^profile/$', views.profile, name='profile'),
]
