from django.http import HttpResponse, Http404, JsonResponse

from tweets.models import Tweet


def home_view(request):
    return HttpResponse("<h1>Hello World</h1>")


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
