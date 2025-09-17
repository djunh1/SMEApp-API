from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone
import random

from portfolios.models import Portfolio, Stock, Review

class Command(BaseCommand):
    help = 'Populates database with portfolios'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        
        """
        # Portfolio #
        """
        for i in range(options['n']):
            name = 'Tonys Swing Portoflio' if random.randint(0, 1) == 0 else ('Dan Zangers portfolio' if random.randint(0, 1) == 0 else 'Stock Bee Special')
            description = 'Solid long term portfolio' if random.randint(0, 1) == 0 else ('Swing trading only' if random.randint(0, 1) == 0 else 'Via Pairoli 33')
            portfolio_type = 'Long Term' if random.randint(0, 1) == 0 else ('Swing' if random.randint(0, 1) == 0 else 'Day Trading')
 
            order = Portfolio.objects.create(
                name = name, 
                description = description,
                portfolio_type = portfolio_type)

            order.save()
           