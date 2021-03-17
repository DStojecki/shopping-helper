from rest_framework import serializers
from .models import Category
from apps.lists.models import ShoppingList


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'shopping_list', 'product_set', 'created_at')

    def create(self, validated_data):
        shopping_list = validated_data.get('shopping_list') \
            if validated_data.get('shopping_list') \
            in ShoppingList.objects.filter(created_by=self.context['request'].user) \
            else None
        try:
            obj = Category.objects.create(
                name=validated_data.get('name'),
                shopping_list=shopping_list,
                created_by=self.context['request'].user
            )
        except Exception:  # TODO: make exceptions more specific
            raise serializers.ValidationError('Provided data is incorrect!')
        return obj

    def update(self, instance, validated_data):
        try:
            instance.name = validated_data.get('name', instance.name)
            shopping_list = validated_data.get('shopping_list')
            instance.shopping_list = shopping_list \
                if shopping_list \
                in ShoppingList.objects.filter(created_by=self.context['request'].user) \
                else instance.shopping_list
            instance.save()
        except Exception:  # TODO: make exceptions more specific
            raise serializers.ValidationError('Provided data is incorrect!')
        return instance
