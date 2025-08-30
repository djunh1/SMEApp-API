from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets

from portfolios.serializers import PortfolioSerializer
from portfolios.models import Portfolio

class PortfoliosOldViewSet(APIView):

    def get(self, request):
        portfolio = {
            'id': 12,
            'title': 'value portfolio'
        }

        return Response(portfolio)
    

class PortfoliosViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return Portfolio.objects.all().order_by('-created_at')