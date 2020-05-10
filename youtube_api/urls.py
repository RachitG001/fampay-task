from django.urls import path
from .views import CricketDataView,DashboardView
from .tasks import api_fetch

urlpatterns = [
    path('get-data/',CricketDataView.as_view()),
    path('dashboard/',DashboardView.as_view())
]


# Comment below line before making migrations.
api_fetch(repeat=100,repeat_until=None)