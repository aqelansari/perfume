from rest_framework import serializers
from inventory.models import IngredientsInventory
from ingredient.models import Ingredient
from ingredient.serializer import IngredientSerializer
from datetime import datetime

class IngredientsInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsInventory
        fields = ['ingredient','quantity','per_unit_price']

    
    def validate_ingredient(self, data):
        ingredient_inventory = Ingredient.objects.filter(id = data.id).exists()
        if ingredient_inventory:
            return data
        else:
            raise serializers.ValidationError("Please Enter Valid Ingredient ID")


class AllIngredientInventorySerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    class Meta:
        model = IngredientsInventory
        fields = ['quantity','per_unit_price','added_on','updated_on','ingredient','added_by','updated_by','ingredient']


    
class UpdateInventoryAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsInventory
        fields = ('quantity','per_unit_price',)
    
    def update(self, instance, validated_data):
        
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.per_unit_price = validated_data.get('per_unit_price', instance.per_unit_price)
        instance.updated_on = validated_data.get('updated_on', instance.updated_on)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.save()
        return instance