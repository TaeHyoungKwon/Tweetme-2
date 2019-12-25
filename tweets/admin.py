from django.contrib import admin

from tweets.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user"]
    search_fields = ["content", "user__username", "user__eamil"]

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)
