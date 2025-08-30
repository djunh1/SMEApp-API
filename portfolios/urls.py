from portfolios.views import PortfoliosViewSet, PortfoliosOldViewSet
from django.urls import include, path
from rest_framework .routers import DefaultRouter

router = DefaultRouter()

router.register('portfolios', PortfoliosViewSet, basename='portfolios')

urlpatterns = [
    path('portfoliosold/', PortfoliosOldViewSet.as_view(), name='portfolios'),
    path('', include(router.urls))

]
