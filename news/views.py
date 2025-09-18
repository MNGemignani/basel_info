from django.contrib.auth.decorators import login_required
from django.core import signing
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.core.paginator import Paginator
from .models import NewsItem
from .rss import fetch_and_store

def news_list(request):
    qs = NewsItem.objects.all()
    paginator = Paginator(qs, 12)
    page = request.GET.get("page")
    items = paginator.get_page(page)
    return render(request, "news/list.html", {"items": items})

@login_required
def refresh_news(request):
    created, updated = fetch_and_store()
    return render(request, "news/refresh_result.html", {"created": created, "updated": updated})

def refresh_news_with_token(request, token):
    try:
        signing.loads(token, salt=settings.REFRESH_SIGNING_SALT, max_age=60*10)  # 10 min TTL token
    except signing.BadSignature:
        return HttpResponseForbidden("Invalid or expired token.")
    created, updated = fetch_and_store()
    return HttpResponse(f"OK. created={created}, updated={updated}")
