from django.contrib import admin
from .models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'updated_at')
    filter_horizontal = ('likes',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('user__username', 'content')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


admin.site.register(Tweet, TweetAdmin)