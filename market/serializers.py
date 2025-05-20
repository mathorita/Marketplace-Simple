from rest_framework import serializers
from .models import Product,Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price','available_quantity','owner']

class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source = 'buyer.id')
    
    class Meta:
        model = Order
        fields = ['id','buyer','product','quantity','created_at']
        read_only_fields=['created_at']
        