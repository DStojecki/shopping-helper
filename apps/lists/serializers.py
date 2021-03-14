from rest_framework import serializers
from .models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'is_archived', 'created_at')

    def create(self, validated_data):
        try:
            obj = ShoppingList.objects.create(
                name=validated_data.get('name'),
                created_by=self.context['request'].user
            )
        except Exception:  # TODO: make exceptions more specific
            raise serializers.ValidationError('Provided data is incorrect!')
        return obj

    def update(self, instance, validated_data):
        try:
            instance.name = validated_data.get('name', instance.name)
            instance.is_archived = validated_data.get('is_archived', instance.is_archived)
            instance.save()
        except Exception:  # TODO: make exceptions more specific
            raise serializers.ValidationError('Provided data is incorrect!')
        return instance
