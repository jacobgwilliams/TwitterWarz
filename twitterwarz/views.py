from django.http import HttpResponse
from django.shortcuts import render
import re
import os
from IPython import embed
from helpers import get_last_tweets, get_user_info
from django.http import JsonResponse

nonalpha_re = re.compile('[^A-Z]')

class RestView(object):
    """
    Subclass this and add GET / POST / etc methods.
    """
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE', 'HEAD', 'OPTIONS')
    
    def __call__(self, request, *args, **kwargs):
        method = nonalpha_re.sub('', request.method.upper())
        if not method in self.allowed_methods or not hasattr(self, method):
            return self.method_not_allowed(method)
        return getattr(self, method)(request, *args, **kwargs)
    
    def method_not_allowed(self, method):
        response = HttpResponse('Method not allowed: %s' % method)
        response.status_code = 405
        return response


def index(request):
    return HttpResponse("Hello, world. You're at the twitterwarz index.")

class GetTweets(RestView):

  def GET(self, request, username):
    last_30_tweets = get_last_tweets(username)
    # embed()
    return render(request, 'timeline.html', {'last_30_tweets': last_30_tweets})

class GetUserInfo(RestView):

  def GET(self, request, username):
    user_info = get_user_info(username)
    # embed()
    return JsonResponse({
      'username': username,
      'location': user_info.location,
      'description': user_info.description,
      'profile_img_url': user_info.profile_image_url,
      'background_img_url': user_info.profile_background_image_url
      })
