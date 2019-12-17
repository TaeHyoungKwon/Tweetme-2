from django.test import TestCase, Client

from tweets.views import home_view


class TestTweetView(TestCase):
    def setUp(self):
        self.c = Client()

    def test_home_view_should_return_hello_world_text(self):
        response = self.c.get("/")
        self.assertEqual(response.content.decode("ascii"), "<h1>Hello World</h1>")

    def test_tweet_detail_view_should_return_hello_world_text_with_tweet_id(self):
        tweet_id = "1"
        response = self.c.get("/tweets/" + tweet_id)
        self.assertEqual(response.content.decode("ascii"), "<h1>Hello 1</h1>")
