from django.contrib.auth.models import User
from django.test import TestCase, Client

from tweets.models import Tweet

MAX_LIKES_COUNT = 200
MIN_LIKES_COUNT = 0


class TestTweetView(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create(username='taehyoung', password='password')
        self.tweet = Tweet.objects.create(content='TweetMe', user=self.user)

    def test_tweet_detail_view_should_raise_404_when_given_tweet_id_is_not_exist(self):
        not_exist_tweet_id = "12345"
        response = self.c.get("/tweets/" + not_exist_tweet_id)
        self.assertEqual(response.status_code, 404)

    def test_tweet_detail_view_should_have_message_string_is_not_found_when_given_tweet_id_is_not_exist(self):
        not_exist_tweet_id = "12345"
        response = self.c.get("/tweets/" + not_exist_tweet_id)
        response = response.json()
        self.assertEqual(response["message"], "Not found")

    def test_tweet_detail_view_should_return_200_when_tweet_instance_is_exist(self):
        response = self.c.get("/tweets/" + str(self.tweet.pk))
        response = response.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["content"], "TweetMe")

    def test_tweet_detail_view_should_return_tweet_id_and_content_when_tweet_instance_is_exist(self):
        response = self.c.get("/tweets/" + str(self.tweet.pk))
        response = response.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["content"], "TweetMe")

    def test_tweet_list_view_should_return_200(self):
        response = self.c.get("/tweets/")
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data["response"][0]["content"], "TweetMe")

    def test_tweet_list_should_return_likes_0_to_122(self):
        response = self.c.get("/tweets/")
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(json_data["response"][0]["likes"], MAX_LIKES_COUNT)
        self.assertGreaterEqual(json_data["response"][0]["likes"], MIN_LIKES_COUNT)

    def test_tweet_create_view_should_be_201_when_given_request_is_ajax(self):
        response = self.c.post("/create-tweet/", HTTP_X_REQUESTED_WITH="XMLHttpRequest", data={"next": "/"})
        self.assertEqual(response.status_code, 201)

    def test_tweet_create_view_should_return_400_when_given_request_is_ajax(self):
        too_long_content = "KwonTaeHyoung" * 1000
        response = self.c.post(
            "/create-tweet/",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
            data={"next": "/", "content": too_long_content},
        )
        self.assertEqual(response.status_code, 400)
