from django.db import models
import uuid


class Portfolio(models.Model):
    # owner = models.ForeignKey(
    #     Profile, null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #tags = models.ManyToManyField('Tag',  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#     LONG_TERM_VALUE = 'Long term holding period'
#     SWING_TRADING = 'Swing trading - Holding higher growth and momentum stocks for weekds to months'
#     ETF_INVESTOR = 'Variable holding periods - Holding various ETFs for various amounts of time.'
#     PORTOFLIO_OPTIONS = [
#         (LONG_TERM_VALUE, _('Long term holding period - Buy and hold for months or years')),
#         (SWING_TRADING, _('Swing trading - Holding higher growth and momentum stocks for weekds to months')),
#         (ETF_INVESTOR, _('Variable holding periods - Holding various ETFs for various amounts of time.')),
#     ]

#     portfolio_type = models.CharField(
#        max_length=200,
#        choices=PORTOFLIO_OPTIONS,
#        default=LONG_TERM_VALUE
#     )

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         ordering = ['name']

#     # @property
#     # def reviewers(self):
#     #     queryset = self.review_set.all().values_list('owner__id', flat=True)
#     #     return queryset
    

# class Review(models.Model):
#     # owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
#     portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
#     body = models.TextField(null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False)


#     def __str__(self):
#         return self.value
    
#     class Meta:
#         ordering = ['-created']

# class Stock(models.Model):
#      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#      portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
#      ticker = name = models.CharField(max_length=8)
#      company_name = models.TextField(null=True, blank=True)
#      created_at = models.DateTimeField(auto_now_add=True)
#      updated_at = models.DateTimeField(auto_now=True)


    
# class Tag(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name