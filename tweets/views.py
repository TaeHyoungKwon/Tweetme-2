from django.http import HttpResponse, Http404

from tweets.models import Tweet


def home_view(request):
    return HttpResponse("<h1>Hello World</h1>")


def tweet_detail_view(request, tweet_id):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except Tweet.DoesNotExist:
        raise Http404
    return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")
`