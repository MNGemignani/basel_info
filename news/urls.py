from django.urls import path
from .views import news_list, refresh_news, refresh_news_with_token

urlpatterns = [
    path("", news_list, name="news_list"),
    path("refresh/", refresh_news, name="news_refresh"),
    path("refresh/<str:token>/", refresh_news_with_token, name="news_refresh_token"),
]
