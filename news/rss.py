import feedparser
from datetime import datetime, timezone
from .models import NewsItem

FEED_URL = "https://www.bzbasel.ch/basel.rss"

def _parse_datetime(entry):
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    if hasattr(entry, "updated_parsed") and entry.updated_parsed:
        return datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
    return None

def fetch_and_store(limit=None):
    feed = feedparser.parse(FEED_URL)
    created, updated = 0, 0

    for i, entry in enumerate(feed.entries):
        if limit is not None and i >= limit:
            break

        guid = getattr(entry, "id", None) or getattr(entry, "guid", None) or getattr(entry, "link", "")
        title = getattr(entry, "title", "(no title)")[:500]
        link = getattr(entry, "link", "")
        summary = getattr(entry, "summary", "")

        published_dt = _parse_datetime(entry)

        obj, is_created = NewsItem.objects.update_or_create(
            guid=guid,
            defaults={
                "title": title,
                "link": link,
                "summary": summary,
                "published": published_dt,
                "source": "BZ Basel",
            },
        )
        if is_created:
            created += 1
        else:
            updated += 1

    return created, updated
