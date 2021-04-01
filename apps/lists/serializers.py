from rest_framework import serializers
from .models import ShoppingList
from ..categories.models import Category
from ..products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product', 'quantity', 'type')


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'color', 'products')


class ShoppingListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'is_archived', 'created_at', 'categories')

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        shopping_list = ShoppingList.objects.create(
            name=validated_data.get('name'),
            created_by=self.context['request'].user
        )
        for category_data in categories_data:
            products_data = category_data.pop('products')
            category = Category.objects.create(list=shopping_list, **category_data)
            for product_data in products_data:
                Product.objects.create(category=category, **product_data)
        return shopping_list

    def update(self, instance, validated_data):
        instance.name = validated_data.pop('name', instance.name)
        instance.is_archived = validated_data.pop('is_archived', instance.is_archived)
        categories_data = validated_data.pop('categories')
        if categories_data:
            instance.categories.clear()
            for category_data in categories_data:
                products_data = category_data.pop('products')
                category = Category.objects.create(list=instance, **category_data)
                instance.categories.add(category)
                for product_data in products_data:
                    category.products.add(Product.objects.create(category=category, **product_data))
        instance.save()
        return instance
