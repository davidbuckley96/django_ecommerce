from rest_framework import serializers
from store.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.Serializer):
    class Meta:
        model = OrderItem
        fields = 'quantity'

