from .serializers import CricketSerializer
from .models import Cricket
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import filters
# Create your views here.

# Custom pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

#Class for get api
class CricketDataView(generics.ListAPIView):
    queryset = Cricket.objects.all().order_by('-publishedAt')
    serializer_class = CricketSerializer
    pagination_class = StandardResultsSetPagination

#Class for dashboard view
class DashboardView(generics.ListAPIView):

    queryset = Cricket.objects.all().order_by()
    serializer_class = CricketSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['publishedAt']
    order_by = ['-publishedAt']
