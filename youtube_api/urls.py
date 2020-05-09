from django.urls import path
from .views import CricketDataView,DashboardView
from .tasks import dbStore

urlpatterns = [
    path('data/',CricketDataView.as_view()),
    path('dashboard/',DashboardView.as_view())
]

dbStore(repeat=100,repeat_until=None)