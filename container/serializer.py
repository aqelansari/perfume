from rest_framework import serializers
from container.models import Container
from ingredient.models import Ingredient

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        container = Container.objects.create(**validated_data)
        return container

    def validate_ingredient(self, data):
        ingredient = Ingredient.objects.filter(id = data.id).exists()
        if ingredient:
            return data
        else:
            raise serializers.ValidationError("This Ingredient Dosen`t exist")

    def validate_name(self, data):
        container_name = Container.objects.filter(name = data).exists()
        if container_name:
            return serializers.ValidationError("This Container Name is Already exists ! ")
        else:
            return data

    def validate_physical_location(self, data):
        container_physical_location = Container.objects.filter(physical_location = data).exists()
        if container_physical_location:
            return serializers.ValidationError("This Location is Already Booked")
        else:
            return data

class ContainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'



class EditContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ('name','volume','physical_location')
    
    def edit(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.volume = validated_data.get('volume', instance.volume)
        instance.save()
        return instance