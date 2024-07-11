
from rest_framework import serializers
from ingredient.models import IngredientIncompatible, IngredientNotes, IngredientType,IngredientApp,Ingredient,IngredientApplications

class IngredientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        ingredient_type = IngredientType.objects.create(**validated_data)
        return ingredient_type
    
    def validate_type_name(self, data):
        ingredient_type = IngredientType.objects.filter(type_name = data).exists()
        if ingredient_type:
            raise serializers.ValidationError("Please Enter Unique Type")
        else:
            return data
        
    def validate_recipe_order(self, data):
        recipe_order = IngredientType.objects.filter(recipe_order = data).exists()
        if recipe_order:
            raise serializers.ValidationError("This recipe order already exist")
        else:
            return data


class AllIngredientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = ['id', 'type_name', 'recipe_order']



class IngredientAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientApp
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        ingredient_app = IngredientApp.objects.create(**validated_data)
        return ingredient_app
    
    def validate_application_name(self, data):
        application_name = IngredientApp.objects.filter(application_name = data).exists()
        if application_name:
            raise serializers.ValidationError("Please Enter Unique Appilication")
        else:
            return data
        

class AllIngredientAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientApp
        fields = ['id', 'application_name']
        
        

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        ingredient = Ingredient.objects.create(**validated_data)
        return ingredient

    def validate_ingredient_type(self, data):
        type = IngredientType.objects.filter(id = data.id).exists()
        if type:
            return data
        else:
            raise serializers.ValidationError("This Ingredient Type Dosen`t exist")
    
    def validate_name(self, data):
        name = Ingredient.objects.filter(name = data).exists()
        if name:
            raise serializers.ValidationError("Please Enter Unique Ingredient name")
        else:
            return data
    
    def validate_ingredient_code(self, data):
        code = Ingredient.objects.filter(ingredient_code = data).exists()
        if code:
            raise serializers.ValidationError("Please Enter Unique Ingregent code")
        else:
            return data


class AllIngredientSerializer(serializers.ModelSerializer):
    ingredient_type = AllIngredientTypeSerializer()
    class Meta:
        model = Ingredient
        fields = ['id', 'name','ingredient_type','threshold_limit','ingredient_code','remarks']
        


class IngredientApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientApplications
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        ingredient_applications = IngredientApplications.objects.create(**validated_data)
        return ingredient_applications
    
    def validate_ingredient(self, data):
        ingredient = Ingredient.objects.filter(id = data.id).exists()
        if ingredient:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid ingredient")
            
    def validate_ingredient_application(self, data):
        ingredient_app = IngredientApp.objects.filter(id = data.id,is_active = True).exists()
        if ingredient_app:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid ingredient app")
            

class IngredientApplicationsListSerializer(serializers.ModelSerializer):
    ingredient = AllIngredientSerializer()
    ingredient_application = AllIngredientAppSerializer()
    class Meta:
        model = IngredientApplications
        fields = ['ingredient', 'ingredient_application']
        


class IngredientNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientNotes
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        ingredient_note = IngredientNotes.objects.create(**validated_data)
        return ingredient_note
    
    def validate_ingredient(self, data):
        ingredient = Ingredient.objects.filter(id = data.id).exists()
        if ingredient:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid ingredient")
            
    def validate(self, data):
        ingredient_id = (data['ingredient'].id)
        notes_id = (data['notes'])
        notes_Idd = IngredientNotes.objects.filter(ingredient = ingredient_id, notes = notes_id).exists()
        if notes_Idd:
            raise serializers.ValidationError("Please Enter Unique Ingregent Note")
        else:
            return data
            

class IngredientNotesListSerializer(serializers.ModelSerializer):
    ingredient = AllIngredientSerializer()
    class Meta:
        model = IngredientNotes
        fields = ['ingredient', 'notes']
        


class IngredientIncompatibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientIncompatible
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        ingredient_incompatible = IngredientIncompatible.objects.create(**validated_data)
        return ingredient_incompatible
    
    def validate_ingredient(self, data):
        ingredient = Ingredient.objects.filter(id = data.id).exists()
        if ingredient:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid ingredient")
            
    def validate_incompatible(self, data):
        incompatible = Ingredient.objects.filter(id = data.id).exists()
        if incompatible:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid ingredient_incompatible")
            

class IngredientIncompatibleListSerializer(serializers.ModelSerializer):
    ingredient = AllIngredientSerializer()
    incompatible = AllIngredientSerializer()
    class Meta:
        model = IngredientApplications
        fields = ['ingredient', 'incompatible']

        