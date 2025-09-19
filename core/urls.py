from django.urls import path
from .views import home, history, university

urlpatterns = [
    path("", home, name="home"),
    path("university/", university, name="university"),
    path("history/", history, name="history"),
]
