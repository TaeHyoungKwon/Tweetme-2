from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from tweets.models import Tweet


def home_view(request):
    return render(request, 'pages/home.html', context={}, status=200)


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
