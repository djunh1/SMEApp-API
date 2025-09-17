from portfolios.views import PortfolioFilterViewSet, PortfolioTypeFilterViewSet, PortfoliosViewSet, StockSectorFilterViewSet, StockViewSet, ReviewViewSet
from django.urls import include, path
from rest_framework .routers import DefaultRouter

router = DefaultRouter()

router.register('portfolios', PortfoliosViewSet, basename='portfolios')
router.register('stocks', StockViewSet, basename='stocks')
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('portfolio-type-filters', PortfolioTypeFilterViewSet, basename='portfolio-type-filters')
router.register('stock-sector-filters', StockSectorFilterViewSet, basename='stock-sector-filters')
router.register('portfolio-filters', PortfolioFilterViewSet, basename='portfolio-filters') # no paginatio

urlpatterns = [
    path('', include(router.urls))
]
