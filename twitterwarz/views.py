from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import re
import os
from IPython import embed
from api_helpers import get_last_tweets, get_user_info, tweets_to_dict
from django.http import JsonResponse
import json
import requests

nonalpha_re = re.compile('[^A-Z]')

class RestView(object):

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

class GetTweets(RestView):

  def GET(self, request, username):
    last_30_tweets = get_last_tweets(username)
    tweet_dict = tweets_to_dict(last_30_tweets)
    return JsonResponse(tweet_dict)

class GetUserInfo(RestView):

  def GET(self, request, username):
    user_info = get_user_info(username)
    return JsonResponse({
      'username': username,
      'location': user_info.location,
      'description': user_info.description,
      'profile_img_url': user_info.profile_image_url,
      'background_img_url': user_info.profile_background_image_url,
      'last_tweet_id': user_info.status.id
      })


def index(request):
    return render(request, 'twitterwarz/index.html')


def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'twitterwarz/profile.html', {'data': parsedData})

def battle(request):
    return render(request, 'twitterwarz/battle.html')
    
