from rest_framework import viewsets

from portfolios.serializers import PortfolioSerializer, ReviewSerializer, StockSerializer
from portfolios.models import Portfolio, Review, Stock


class PortfoliosViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return Portfolio.objects.all().order_by('-created_at')
    
class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class StockViewSet(viewsets.ModelViewSet):

    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.all().order_by('-ticker_name', 'sector')
    