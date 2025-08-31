from portfolios.views import PortfoliosViewSet, StockViewSet, ReviewViewSet
from django.urls import include, path
from rest_framework .routers import DefaultRouter

router = DefaultRouter()

router.register('portfolios', PortfoliosViewSet, basename='portfolios')
router.register('stocks', StockViewSet, basename='stocks')
router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls))
]
