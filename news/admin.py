from django.contrib import admin
from .models import NewsItem

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "source")
    search_fields = ("title", "summary")
    list_filter = ("source",)
