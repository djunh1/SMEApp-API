from rest_framework import serializers

from portfolios.models import Category, Portfolio, Review, Stock, Tag

# TODO-1 eventually add owner to fields.
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id',
                  'name',
                  'description',
                  'created_at',
                  'updated_at',
                  'category',
                  'tags'
                  ]
        
    def to_representation(self, instance):
        self.fields['category'] =  CategorySerializer(read_only=True)
        return super(PortfolioSerializer, self).to_representation(instance)
        
    # def to_representation(self, instance):
    #     self.fields['owner'] = OwnerSerializer(read_only=True)
    #     return super().to_representation(instance)

# TODO-1 eventually add owner to fields.        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id',
                  'body',
                  'portfolio',
                  'created'
                  ]
    def to_representation(self, instance):
  #     self.fields['owner'] = OwnerSerializer(read_only=True)
        self.fields['portfolio'] = PortfolioSerializer(read_only=True) 
        return super(ReviewSerializer, self).to_representation(instance)
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id',
                  'portfolio',
                  'ticker_name',
                  'company_name',
                  'sector',
                  'created_at'
                  ]
        
    def to_representation(self, instance):
        self.fields['portfolio'] = PortfolioSerializer(read_only=True) 
        return super(StockSerializer, self).to_representation(instance)
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id',
                  'name'
                  ]
        
class PortfolioTypeFilterSerializer(serializers.ModelSerializer):
    '''
    Specific search for portfolio type 
    '''
    class Meta:
        model = Portfolio
        fields = ['portfolio_type']

class StockSectorFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['sector']

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name']

class CategorySerializerId(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id']