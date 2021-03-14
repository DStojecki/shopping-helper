from rest_framework import serializers
from .models import Product
from apps.categories.models import Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'quantity', 'quantity_type', 'created_at')

    def create(self, validated_data):
        category = validated_data.get('category') \
            if validated_data.get('category') \
            in Category.objects.filter(created_by=self.context['request'].user) \
            else None
        try:
            obj = Product.objects.create(
                name=validated_data.get('name'),
                category=category,
                quantity=validated_data.get('quantity'),
                quantity_type=validated_data.get('quantity_type'),
                created_by=self.context['request'].user
            )
        except Exception:  # TODO: make exceptions more specific
            raise serializers.ValidationError('Provided data is incorrect!')
        return obj

    def update(self, instance, validated_data):
        category = validated_data.get('category') \
            if validated_data.get('category') \
            in Category.objects.filter(created_by=self.context['request'].user) \
            else instance.category
        try:
            instance.name = validated_data.get('name', instance.name)
            instance.category = category
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.quantity_type = validated_data.get('quantity_type', instance.quantity_type)
            instance.save()
        except Exception:  # TODO: make exceptions more specific
            raise serializers.ValidationError('Provided data is incorrect!')
        return instance
