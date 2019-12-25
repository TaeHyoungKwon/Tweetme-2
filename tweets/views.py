import random

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

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
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, "components/form.html", context={"form": form})


def tweet_list_view(request):
    tweets = Tweet.objects.all()
    tweet_list = [tweet.serialize() for tweet in tweets]
    tweet_list_data = {"isUser": False, "response": tweet_list}
    return JsonResponse(tweet_list_data, status=200)
