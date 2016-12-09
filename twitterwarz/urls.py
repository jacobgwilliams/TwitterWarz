from django.conf.urls import url

from . import views
from views import OurTwitterApi

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^twitter_user/(.+)$', OurTwitterApi()),
]
