from rest_framework import serializers

from tweetme2 import settings
from tweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["content"]

    @staticmethod
    def validate_content(value):
        if len(value) > settings.MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value
