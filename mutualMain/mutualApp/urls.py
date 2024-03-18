from django.urls import path
from . import views

app_name = "mutualApp"

urlpatterns = [
    path("consistent_returns/", views.consistent_returns, name="consistent_returns"),
    path("learn-more/", views.learn_more, name="learn_more"),
    path("age-cal/", views.addCalculatorAge, name="addCalculatorAge"),
]