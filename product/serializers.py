from rest_framework import serializers
from .models import Product, ProductImage, AttributeCategory, AttributeValue


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ['title', 'value', 'image']


class AttributeNameSerializer(serializers.ModelSerializer):
    attribute_values = AttributeValueSerializer(many=True, read_only=True)

    class Meta:
        model = AttributeCategory
        fields = ['name', 'attribute_values']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'product_images']


class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    attribute_names = AttributeNameSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'product_images', 'attribute_names']
