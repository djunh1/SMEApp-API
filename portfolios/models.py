from django.db import models
import uuid

### TODO-1: Add owner once the custom user is created

PORTOFLIO_TYPE = (
    ('Long Term', 'Long term - hold periods of months to years'),
    ('Swing', 'Swing - hold periods of weeks to months'),
    ('Variable', 'Variable time frames'),
    ('Day Trading', 'Day trading - Short hold times of one day or less'),
)

class Portfolio(models.Model):
    # owner = models.ForeignKey(
    #     Profile, null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    portfolio_type = models.CharField(max_length=200, choices=PORTOFLIO_TYPE, default='Combination of shorter time frames and longer time frames')
    tags = models.ManyToManyField('Tag',  blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

    # @property
    # def reviewers(self):
    #     queryset = self.review_set.all().values_list('owner__id', flat=True)
    #     return queryset
    

class Review(models.Model):
    # owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    body = models.TextField(null=True, blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.value
    
    class Meta:
        ordering = ['-created']

class Stock(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
     portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
     ticker_name = models.CharField(max_length=8)
     company_name = models.TextField(null=True, blank=True)
     sector = models.TextField(null=True, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.portfolio + '_' + self.ticker_name
     
     class Meta:
        ordering = ['ticker_name']


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name