# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 15:53
from __future__ import unicode_literals

import datetime

from faker import Faker
fake = Faker()
from random import randint

from django.db import models, migrations

def load_users(twitterwarz, schema_editor):
  User = twitterwarz.get_model('twitterwarz', 'User')
  jacob = User(twitter_handle='jacobstweets', email='jacob@aol.com', password_hash='password', last_tweet_retrieval=datetime.date(2016,9,15))
  jacob.save()
  scott = User(twitter_handle='realscottdixon', email='scott@hotmail.com', password_hash='password', last_tweet_retrieval=datetime.date(2016,8,23))
  scott.save()
  cat = User(twitter_handle='catherinekhuu', email='cat@juno.com', password_hash='password', last_tweet_retrieval=datetime.date(2016,9,13))
  cat.save()
  bb = User(twitter_handle='realbuffalobill', email='buff@msn.com', password_hash='password', last_tweet_retrieval=datetime.date(2016,7,13))
  bb.save()
  trump = User(twitter_handle='realdonaldtrump', email='dj@geocities.com', password_hash='password', last_tweet_retrieval=datetime.date(2016,10,13))
  trump.save()
  phil = User(twitter_handle='dbcphil', email='phil@aol.com', last_tweet_retrieval=datetime.date(2016,10,14))
  phil.save()
  kanye = User(twitter_handle='kanye', email='kanye@kanye.com', last_tweet_retrieval=datetime.date(2016,10,14))
  kanye.save()
  angela = User(twitter_handle='angela_merkel', email='angela@germany.com', last_tweet_retrieval=datetime.date(2016,10,14))
  angela.save()
  for x in range(0, 10):
    user = User(twitter_handle=fake.first_name().lower(), email=fake.email(), last_tweet_retrieval=fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None))
    user.save()

def load_tweets(twitterwarz, schema_editor):
  Tweet= twitterwarz.get_model('twitterwarz', 'Tweet')
  t_one = Tweet(user_id=1, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=3, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=7, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=8, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=8, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=8, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=1, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=1, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=1, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=4, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=3, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=3, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=3, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=3, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=3, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=5, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=6, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=7, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=7, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=7, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like turtles')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  t_one = Tweet(user_id=2, date=datetime.datetime.now(), content='I like meat')
  t_one.save()
  for x in range(0, 100):
    t = Tweet(user_id=randint(1,18), content=("I love being a " + fake.job()), date=fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None))
    t.save

class Migration(migrations.Migration):

    dependencies = [
        ('twitterwarz', '0003_auto_20161208_2329'),
    ]

    operations = [
      migrations.RunPython(load_users),
      migrations.RunPython(load_tweets)
    ]