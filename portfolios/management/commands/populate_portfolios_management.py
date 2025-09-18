from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone
import random

from portfolios.models import Category, Portfolio, Stock, Review

class Command(BaseCommand):
    help = 'Populates database with portfolios'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):

        """
        # Category #
        """
        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category4 = Category.objects.get(pk=4)
        
        """
        # Portfolio #
        """
        for i in range(options['n']):
            category = category1 

            name = 'Tonys Swing Portoflio' if random.randint(0, 1) == 0 else ('Dan Zangers portfolio' if random.randint(0, 1) == 0 else 'Stock Bee Special')
            description = 'Solid long term portfolio' if random.randint(0, 1) == 0 else ('Swing trading only' if random.randint(0, 1) == 0 else 'Via Pairoli 33')
            portfolio_type = 'Long Term' if random.randint(0, 1) == 0 else ('Swing' if random.randint(0, 1) == 0 else 'Day Trading')
 
            order = Portfolio.objects.create(
                name = name, 
                description = description,
                portfolio_type = portfolio_type,
                category = category)

            order.save()

        """
        # Portfolio #
        """
        for i in range(options['n']):
            category = category2

            name = 'Dougs Swing Portoflio' if random.randint(0, 1) == 0 else ('Pradeeps portfolio' if random.randint(0, 1) == 0 else 'Wu tang ifnancial')
            description = 'Solid long term portfolio' if random.randint(0, 1) == 0 else ('Swing trading only' if random.randint(0, 1) == 0 else 'Via Pairoli 33')
            portfolio_type = 'Long Term' if random.randint(0, 1) == 0 else ('Swing' if random.randint(0, 1) == 0 else 'Day Trading')
 
            order = Portfolio.objects.create(
                name = name, 
                description = description,
                portfolio_type = portfolio_type,
                category = category)

            order.save()

        """
        # Portfolio #
        """
        for i in range(options['n']):
            category = category2

            name = 'Dougs Swing Portoflio' if random.randint(0, 1) == 0 else ('Pradeeps portfolio' if random.randint(0, 1) == 0 else 'Wu tang ifnancial')
            description = 'Solid long term portfolio' if random.randint(0, 1) == 0 else ('Swing trading only' if random.randint(0, 1) == 0 else 'Via Pairoli 33')
            portfolio_type = 'Long Term' if random.randint(0, 1) == 0 else ('Swing' if random.randint(0, 1) == 0 else 'Day Trading')
 
            order = Portfolio.objects.create(
                name = name, 
                description = description,
                portfolio_type = portfolio_type,
                category = category)

            order.save()
           