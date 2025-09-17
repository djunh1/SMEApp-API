from rest_framework import viewsets

from portfolios.serializers import PortfolioSerializer, PortfolioTypeFilterSerializer, ReviewSerializer, StockSectorFilterSerializer, StockSerializer
from portfolios.models import Portfolio, Review, Stock

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PortfoliosViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioSerializer
    filter_backends = {DjangoFilterBackend, filters.SearchFilter}

    filterset_fields = ['name', 'portfolio_type']

    def get_queryset(self):
        if(self.request.GET.get('order_by')) == 'updated_at':
            return Portfolio.objects.all().order_by('-updated_at')
        else:
            return Portfolio.objects.all().order_by('portfolio_type')
    
class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class StockViewSet(viewsets.ModelViewSet):

    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # search all stocks by filtering a portfolio type, in this case
    search_fields = ['portfolio__portfolio_type']

    def get_queryset(self):
        if (self.request.GET.get('order_by')) == 'sector':
            return Stock.objects.all().order_by('-sector')
        elif (self.request.GET.get('order_by')) == 'company_name':
            return Stock.objects.all().order_by('-company_name')
        elif (self.request.GET.get('order_by')) == 'updated_at':
            return Stock.objects.all().order_by('-updated_at')
        else:
            return Stock.objects.all().order_by('-ticker_name')

class PortfolioTypeFilterViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.values('portfolio_type').distinct()
    serializer_class = PortfolioTypeFilterSerializer
    paginator = None

class StockSectorFilterViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.values('sector').distinct()
    serializer_class = StockSectorFilterSerializer
    paginator = None

class PortfolioFilterViewSet(viewsets.ModelViewSet): 
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    paginator = None