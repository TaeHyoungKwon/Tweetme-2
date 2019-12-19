from django.test import TestCase, Client

from tweets.models import Tweet
from tweets.views import home_view


class TestTweetView(TestCase):
    def setUp(self):
        self.c = Client()

    def test_tweet_detail_view_should_raise_404_when_given_tweet_id_is_not_exist(self):
        Tweet.objects.create(content="TweetMe")
        not_exist_tweet_id = "12345"
        response = self.c.get("/tweets/" + not_exist_tweet_id)
        self.assertEqual(response.status_code, 404)

    def test_tweet_detail_view_should_have_message_string_is_not_found_when_given_tweet_id_is_not_exist(self):
        Tweet.objects.create(content="TweetMe")
        not_exist_tweet_id = "12345"
        response = self.c.get("/tweets/" + not_exist_tweet_id)
        response = response.json()
        self.assertEqual(response["message"], "Not found")

    def test_tweet_detail_view_should_return_200_when_tweet_instance_is_exist(self):
        tweet_instance = Tweet.objects.create(content="TweetMe")
        response = self.c.get("/tweets/" + str(tweet_instance.pk))
        response = response.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["content"], "TweetMe")

    def test_tweet_detail_view_should_return_tweet_id_and_content_when_tweet_instance_is_exist(self):
        tweet_instance = Tweet.objects.create(content="TweetMe")
        response = self.c.get("/tweets/" + str(tweet_instance.pk))
        response = response.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["content"], "TweetMe")

    def test_tweet_list_view_should_return_200(self):
        Tweet.objects.create(content="TweetMe")
        response = self.c.get("/tweets/")
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data["response"][0]["content"], "TweetMe")
