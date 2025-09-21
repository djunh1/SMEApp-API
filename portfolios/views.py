from rest_framework import viewsets

from portfolios.serializers import CategorySerializer, CategorySerializerId, PortfolioSerializer, PortfolioTypeFilterSerializer, ReviewSerializer, StockSectorFilterSerializer, StockSerializer
from portfolios.models import Category, Portfolio, Review, Stock

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PortfoliosViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioSerializer
    filter_backends = {DjangoFilterBackend, filters.SearchFilter}

    filterset_fields = ['name']
    search_fields = ['category__name']

    def get_queryset(self):
        if(self.request.GET.get('order_by')) == 'updated_at':
            return Portfolio.objects.all().order_by('-updated_at')
        else:
            return Portfolio.objects.all().order_by('name')
    
class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class StockViewSet(viewsets.ModelViewSet):

    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # search all stocks by filtering a portfolio type, in this case
    #TODO add more later. 
    # filterset_fields = ['ticker_name']
    search_fields = ['portfolio__name']

    def get_queryset(self):
        if (self.request.GET.get('order_by')) == 'sector':
            return Stock.objects.all().order_by('-sector')
        elif (self.request.GET.get('order_by')) == 'company_name':
            return Stock.objects.all().order_by('-company_name')
        elif (self.request.GET.get('order_by')) == 'created_at':
            return Stock.objects.all().order_by('-created_at')
        else:
            return Stock.objects.all().order_by('ticker_name')

class PortfolioTypeFilterViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.values('category').distinct()
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

class CategoryViewSet(viewsets.ModelViewSet):
    '''
    This populates the portfolio create and edit modals.
    '''
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryViewSetNotPaged(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    paginator = None

class CategoryViewSetNotPagedId(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializerId
    paginator = None