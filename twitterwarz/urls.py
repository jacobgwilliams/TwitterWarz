from django.conf.urls import url

from twitterwarz import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test')
]
