from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime

from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class User(models.Model):
    twitter_handle = models.CharField(max_length=60)
    email = models.CharField(max_length=80)
    password_hash = models.CharField(max_length=30)
    last_tweet_retrieval = models.DateTimeField('last tweet retrieval')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.twitter_handle

@python_2_unicode_compatible
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    date = models.DateTimeField('tweet timestamp')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content

class Battle(models.Model):
    attacker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attacker')
    defender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='defender')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner')
    loser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loser')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
