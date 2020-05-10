from django.urls import path
from .views import CricketDataView,DashboardView
from .tasks import db_store

urlpatterns = [
    path('get-data/',CricketDataView.as_view()),
    path('dashboard/',DashboardView.as_view())
]


# Comment below line before making migrations.
db_store(repeat=100,repeat_until=None)