from django.urls import path

from core import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
]
