from django.urls import path
from .views import home, university

urlpatterns = [
    path("", home, name="home"),
    path("university/", university, name="university"),
]
