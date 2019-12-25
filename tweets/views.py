import random

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from serializers import TweetSerializer
from tweetme2.settings import ALLOWED_HOSTS
from tweets.forms import TweetForm
from tweets.models import Tweet


def home_view(request):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_detail_view(request, tweet_id):
    data = {"id": tweet_id}
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except Tweet.DoesNotExist:
        data["message"] = "Not found"
        status = 404
    return JsonResponse(data, status=status)


def tweet_create_view(request):
    serializer = TweetSerializer(data=request.POST or None)
    user = User.objects.all()[0]
    if serializer.is_valid():
        serializer.save(user=user)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({}, status=400)


def tweet_list_view(request):
    tweets = Tweet.objects.all()
    tweet_list = [tweet.serialize() for tweet in tweets]
    tweet_list_data = {"isUser": False, "response": tweet_list}
    return JsonResponse(tweet_list_data, status=200)
