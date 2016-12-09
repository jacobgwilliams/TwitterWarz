from rest_framework import serializers
from .models import User, Tweet, Battle

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
