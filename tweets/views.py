from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tweets.models import Tweet
from tweets.serializers import TweetSerializer


def home_view(request):
    return render(request, "pages/home.html", context={}, status=200)


@api_view(["GET"])
def tweet_detail_view(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TweetSerializer(tweet)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def tweet_create_view(request):
    serializer = TweetSerializer(data=request.POST or None)
    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def tweet_list_view(request):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
