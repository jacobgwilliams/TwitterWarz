import tweepy
import os
from django.http import JsonResponse
from IPython import embed
from models import User

CONSUMER_KEY = os.environ['consumer_key']
CONSUMER_SECRET = os.environ['consumer_secret']
ACCESS_TOKEN = os.environ['access_token']
ACCESS_TOKEN_SECRET = os.environ['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
tweepy_api = tweepy.API(auth)

def get_last_tweets(username):
  # This method takes in a 'since_id' that acts like our 'last_tweet_retrieval'
  # if we change that from being a timestamp, to being the id...
  # user = User.objects.get(twitter_handle=username)
  # return tweepy_api.user_timeline(username, since_id=user.last_tweet_id)
  return tweepy_api.user_timeline(username, count=30)

def get_user_info(username):
  return tweepy_api.get_user(username)

def tweets_to_dict(tweet_array):
  tweet_dict = {}

  for tweet in tweet_array:
    tweet_dict[tweet.id] = {}
    tweet_dict[tweet.id]['content'] = tweet.text
    tweet_dict[tweet.id]['timestamp'] = tweet.created_at
    if 'media' in tweet.entities.keys():
      tweet_dict[tweet.id]['pic_url'] = tweet.entities['media'][0]['media_url']
    else:
      tweet_dict[tweet.id]['pic_url'] = None

  return tweet_dict
