from django.contrib.auth.models import User
from django.test import TestCase, Client

from tweets.models import Tweet

MAX_LIKES_COUNT = 200
MIN_LIKES_COUNT = 0


class TestDRFAPI(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        self.tweet = Tweet.objects.create(content='THKWON')

    def test_tweet_list_view_should_return_status_code_is_200(self) -> None:
        # When: Call tweet_list_view
        response = self.c.get("/tweets/")
        # Then: tweet_list_view should return status_code is 200
        self.assertEqual(response.status_code, 200)

    def test_tweet_detail_view_should_return_status_code_is_404_when_tweet_is_not_exists(self) -> None:
        # Given: Set tweet_id
        can_not_fount_tweet_id = '404'
        # When: Call tweet_detail_view
        response = self.c.get("/tweets/" + can_not_fount_tweet_id + "/")
        # Then: tweet_detail_view should return status_code is 404
        self.assertEqual(response.status_code, 404)

    def test_tweet_detail_view_should_return_status_code_is_200_when_tweet_is_exists(self) -> None:
        # Given: Set tweet_id
        tweet_id = '1'
        # When: Call tweet_detail_view
        response = self.c.get("/tweets/" + tweet_id + "/")
        # Then: tweet_detail_view should return status_code is 404
        self.assertEqual(response.status_code, 200)

    def test_tweet_create_view_should_be_400_when_serializer_is_invalid(self):
        invalid_content = "too_long_content" * 100
        response = self.c.post("/create-tweet/", data={"next": "/", "content": invalid_content})
        self.assertEqual(response.status_code, 400)

    def test_tweet_create_view_should_be_200_when_serializer_is_valid(self):
        valid_content = "valid content"
        response = self.c.post("/create-tweet/", data={"next": "/", "content": valid_content})
        self.assertEqual(response.status_code, 201)