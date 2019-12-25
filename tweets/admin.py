from django.contrib import admin

from tweets.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["content"]

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)
