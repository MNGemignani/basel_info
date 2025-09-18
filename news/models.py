from django.db import models

class NewsItem(models.Model):
    guid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=500)
    link = models.URLField()
    summary = models.TextField(blank=True)
    published = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=255, default="BZ Basel")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published", "-created_at"]

    def __str__(self):
        return self.title
