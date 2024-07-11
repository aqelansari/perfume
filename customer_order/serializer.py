from rest_framework import serializers
from django.contrib.auth.models import User
from customer_order.models import CustomerOrder,OrderSteps
from recipe.models import Recipe
from recipe.serializer import RecipeSerializer
from company.models import WorkStation
from company.serializer import WorkstationSerializer


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'

    def validate_recipe(self, data):
        recipe = Recipe.objects.filter(id=data.id).exists()
        if recipe:
            return data
        else:
            return serializers.ValidationError("Please Enter valid recipe")

    def validate_assigned_to(self, data):
        order_volume = User.objects.filter(id=data.id).exists()
        if order_volume:
            return data
        else:
            return serializers.ValidationError("Please Enter Valid user")

    def validate_production_place(self, data):
        production_place = WorkStation.objects.filter(id=data.id).exists()
        if production_place:
            return data
        else:
            return serializers.ValidationError("Please Enter Valid production place")


class AllCustomerOrderSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer()
    production_place = WorkstationSerializer()
    class Meta:
        model = CustomerOrder
        fields = ['order_volume', 'assigned_to', 'order_status', 'remarks', 'added_on', 'added_by', 'updated_on', 'updated_by', 'recipe', 'production_place']


class UpdateCustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ('id','order_volume','assigned_to','production_place','order_status','remarks','recipe')
    
    def update(self, instance, validated_data):
        
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.order_volume = validated_data.get('order_volume', instance.order_volume)
        instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
        instance.production_place = validated_data.get('production_place', instance.production_place)
        instance.order_status = validated_data.get('order_status', instance.order_status)
        instance.remarks = validated_data.get('remarks', instance.remarks)
        instance.updated_on = validated_data.get('updated_on', instance.updated_on)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.save()
        return instance


class OrderStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSteps
        fields = '__all__'

    def validate_order_steps(self, data):
        order_steps = CustomerOrder.objects.filter(id=data.id).exists()
        if order_steps:
            return data
        else:
            return serializers.ValidationError("Please Enter valid Oder")


class AllOrderStepsSerializer(serializers.ModelSerializer):
    customer_order= CustomerOrderSerializer()
    class Meta:
        model = OrderSteps
        fields = ['step_info','step_number','start_time','end_time','step_status','customer_order']


    

