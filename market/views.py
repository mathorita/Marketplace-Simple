from django.shortcuts import render
from .models import Order,Product
from .serializers import OrderSerializer,ProductSerializer
from rest_framework import viewsets,serializers
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)
    
    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        

        if quantity > product.available_quantity:
            raise serializers.ValidationError('Quantity higher than stock')
        
        product.available_quantity -= quantity
        product.save()

        serializer.save(buyer=self.request.user)