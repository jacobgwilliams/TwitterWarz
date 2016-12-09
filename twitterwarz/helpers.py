import tweepy
import os

CONSUMER_KEY = os.environ['consumer_key']
CONSUMER_SECRET = os.environ['consumer_secret']
ACCESS_TOKEN = os.environ['access_token']
ACCESS_TOKEN_SECRET = os.environ['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
tweepy_api = tweepy.API(auth)

def get_last_tweets(username):
  return tweepy_api.user_timeline(username, count=30)

def get_user_info(username):
  return tweepy_api.get_user(username)