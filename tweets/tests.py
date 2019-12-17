from django.test import TestCase, Client

from tweets.models import Tweet
from tweets.views import home_view


class TestTweetView(TestCase):
    def setUp(self):
        self.c = Client()

    def test_home_view_should_return_hello_world_text(self):
        response = self.c.get("/")
        self.assertEqual(response.content.decode("ascii"), "<h1>Hello World</h1>")

    def test_tweet_detail_view_should_raise_404_when_given_tweet_id_is_not_exist(self):
        Tweet.objects.create(content="TweetMe")
        not_exist_tweet_id = "not_exist_tweet_id"
        response = self.c.get("/tweets/" + not_exist_tweet_id)
        self.assertEqual(response.status_code, 404)

    def test_tweet_detail_view_should_return_hello_string_with_tweet_id_and_obj_content(self):
        tweet_instance = Tweet.objects.create(content="TweetMe")
        response = self.c.get("/tweets/" + str(tweet_instance.pk))
        self.assertEqual(response.content.decode("ascii"), "<h1>Hello 1 - TweetMe</h1>")
