from ingredient.models import Ingredient
from ingredient.serializer import AllIngredientSerializer
from rest_framework import serializers
from recipe.models import RecipeType,RecipeActivity,Recipe,RecipeIngredient,RecipeActivities,RecipeSequence
from ingredient.models import Ingredient,IngredientNotes

class RecipeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeType
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        recipe_type = RecipeType.objects.create(**validated_data)
        return recipe_type
    
    def validate_name(self, data):
        recipe_type = RecipeType.objects.filter(name = data).exists()
        if recipe_type:
            raise serializers.ValidationError("Please Enter Unique Type")
        else:
            return data
class AllRecipeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeType
        fields = '__all__'


class RecipeActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeActivity
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        recipe_activity = RecipeActivity.objects.create(**validated_data)
        return recipe_activity
    
    def validate_name(self, data):
        recipe_name = RecipeActivity.objects.filter(name = data).exists()
        if recipe_name:
            raise serializers.ValidationError("Please Enter Unique Activity")
        else:
            return data
class AllRecipeActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeActivity
        fields = '__all__'
        
        
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        recipe = Recipe.objects.create(**validated_data)
        return recipe

    def validate_recipe_type(self, data):
        name = RecipeType.objects.filter(id = data.id).exists()
        if name:
            return data
        else:
            raise serializers.ValidationError("Please Enter Valid Recipe Type ID")
    
    def validate_name(self, data):
        name = Recipe.objects.filter(name = data).exists()
        if name:
            raise serializers.ValidationError("Please Enter Unique Recipe name")
        else:
            return data

class AllRecipeSerializer(serializers.ModelSerializer):
    recipe_type = AllRecipeTypeSerializer()
    class Meta:
        model = Recipe
        fields = ['id', 'name','recipe_type']
        
        
class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

    def create(self, validated_data):
        recipe_ingredient = RecipeIngredient.objects.create(**validated_data)
        return recipe_ingredient
    
    
    def validate_recipe(self, data):
        recipe = Recipe.objects.filter(id = data.id).exists()
        if recipe:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid Recipe")
            
    
    def validate_ingredient(self, data):
        ingredient = Ingredient.objects.filter(id = data.id).exists()
        if ingredient:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid ingredient")
            

class RecipeIngredientListSerializer(serializers.ModelSerializer):
    recipe = AllRecipeSerializer()
    ingredient = AllIngredientSerializer()
    class Meta:
        model = RecipeIngredient
        fields = ['parts', 'recipe', 'ingredient']
        

class RecipeActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeActivities
        fields = '__all__'

    def create(self, validated_data):
        recipe_activities = RecipeActivities.objects.create(**validated_data)
        return recipe_activities
    
    
    def validate_recipe(self, data):
        recipe = Recipe.objects.filter(id = data.id).exists()
        if recipe:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid Recipe")
            
    
    def validate_activity(self, data):
        activity = RecipeActivity.objects.filter(id = data.id).exists()
        if activity:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid RecipeActivity")
            
class RecipeActivitiesListSerializer(serializers.ModelSerializer):
    recipe = AllRecipeSerializer()
    activity = AllRecipeActivitySerializer()
    class Meta:
        model = RecipeActivities
        fields = ['duration', 'remarks','recipe','activity']


class RecipeSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeSequence
        fields = '__all__'

    def create(self, validated_data):
        recipe_sequence = RecipeSequence.objects.create(**validated_data)
        return recipe_sequence

    def validate_sequence_number(self, data):
        sequence_number = RecipeSequence.objects.filter(sequence_number = data).exists()
        if sequence_number:
            raise serializers.ValidationError("Please Enter Unique sequence_number")
        else:
            return data
    
    def validate_recipe(self, data):
        recipe = Recipe.objects.filter(id = data.id).exists()
        if recipe:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid recipe")   
    
    def validate_Activities(self, data):
        Activities = RecipeActivities.objects.filter(id = data.id).exists()
        if Activities:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid Activities")

    def validate_ingredient(self, data):
        ingredient = Ingredient.objects.filter(id = data.id).exists()
        if ingredient:
            return data
        else:
            raise serializers.ValidationError("Please Enter valid ingredient")
            
class RecipeSequenceListSerializer(serializers.ModelSerializer):
    recipe = AllRecipeSerializer()
    activity = RecipeActivitiesListSerializer()
    ingredient = AllIngredientSerializer()
    class Meta:
        model = RecipeSequence
        fields = ['sequence_number','recipe', 'activity','ingredient']