from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from recipe.serializer import RecipeTypeSerializer,AllRecipeTypeSerializer,RecipeActivitySerializer,AllRecipeActivitySerializer,\
                                RecipeSerializer,AllRecipeSerializer,RecipeIngredientSerializer,RecipeIngredientListSerializer,\
                                RecipeActivitiesSerializer,RecipeActivitiesListSerializer,RecipeSequenceSerializer,RecipeSequenceListSerializer
from recipe.models import RecipeType, RecipeActivity, Recipe,RecipeIngredient,RecipeActivities,RecipeSequence
from ingredient.models import IngredientNotes,Ingredient
from inventory.serializer import AllIngredientInventorySerializer,IngredientsInventorySerializer
from inventory.models import IngredientsInventory
import pdb

class RecipeTypeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            recipe_type_serializer = RecipeTypeSerializer(
                context={'request': request}, data=request.data)
            if recipe_type_serializer.is_valid():
                recipe_type_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': recipe_type_serializer.data}, status=200)
            else:
                return Response({'error': recipe_type_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)

class RecipeTypeListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_recipe_type = RecipeType.objects.filter(
            is_active=True).order_by('-id')
        res = AllRecipeTypeSerializer(all_recipe_type, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)


class RecipeActivityAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            recipe_activity_serializer = RecipeActivitySerializer(
                context={'request': request}, data=request.data)
            if recipe_activity_serializer.is_valid():
                recipe_activity_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': recipe_activity_serializer.data}, status=200)
            else:
                return Response({'error': recipe_activity_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)

class RecipeActivityListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_recipe_activity = RecipeActivity.objects.filter(
            is_active=True).order_by('-id')
        res = AllRecipeActivitySerializer(all_recipe_activity, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)


class RecipeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            recipe_serializer = RecipeSerializer(
                context={'request': request}, data=request.data)
            if recipe_serializer.is_valid():
                recipe_serializer.save()

                return Response(
                    {'error': '', 'error_code': '', 'data': recipe_serializer.data}, status=200)
            else:
                return Response(
                    {'error': recipe_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response(
                        {'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class RecipeListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_recipes = Recipe.objects.filter(is_active=True).order_by('-id')
        res = AllRecipeSerializer(all_recipes, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)
        

class RecipeIngredientAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            recipe_ingredient_serializer = RecipeIngredientSerializer(
                context={'request': request}, data=request.data)
            if recipe_ingredient_serializer.is_valid():
                recipe_ingredient_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': recipe_ingredient_serializer.data}, status=200)
            else:
                return Response({'error': recipe_ingredient_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)

class RecipeIngredientListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_recipes_ingredient = RecipeIngredient.objects.all().order_by('-id')
        res = RecipeIngredientListSerializer(all_recipes_ingredient, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)


class RecipeActivitiesAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            recipe_activities_serializer = RecipeActivitiesSerializer(
                context={'request': request}, data=request.data)
            if recipe_activities_serializer.is_valid():
                recipe_activities_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': recipe_activities_serializer.data}, status=200)
            else:
                return Response({'error': recipe_activities_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)

class RecipeActivitiesListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_recipes_activities = RecipeActivities.objects.all().order_by('-id')
        res = RecipeActivitiesListSerializer(all_recipes_activities, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)


class RecipeSequenceAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            recipe_sequence_serializer = RecipeSequenceSerializer(
                context={'request': request}, data=request.data)
            if recipe_sequence_serializer.is_valid():
                recipe_sequence_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': recipe_sequence_serializer.data}, status=200)
            else:
                return Response({'error': recipe_sequence_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)

class RecipeSequenceListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_recipes_sequence = RecipeSequence.objects.all().order_by('-id')
        res = RecipeSequenceListSerializer(all_recipes_sequence, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)


class IngredientNotesSearchAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data_list = []
        notes_list = []
        ingredient_model = Ingredient.objects.filter(is_active=True).order_by('-id')
        for ingredient in ingredient_model:
            ingredient_dict = dict()
            ingredient_id = ingredient.id
            ingredient_name = ingredient.name
            ingredient_dict['ingredient_id'] = ingredient_id
            ingredient_dict['ingredient_name'] = ingredient_name
            notes_list.append(ingredient_dict)

            nt = []
            ingredient_notes = IngredientNotes.objects.filter(ingredient_id = ingredient_id)
            for notes in ingredient_notes:
                note = notes.notes
                nt.append(note)
                ingredient_dict['note'] = nt
            max_num = []
            ingredient_price = IngredientsInventory.objects.filter(ingredient_id = ingredient_id)
            for price in ingredient_price:
                pr = price.per_unit_price
                max_num.append(pr)
                ingredient_dict['pr'] = max(max_num)

        notes_list.append(ingredient_dict)
        # notes_list.append(ingredient_dict)
        data_list.append(notes_list)  
        return Response({'error': '', 'error_code': '', 'data': data_list}, status=200)
    

class DeleteRecipeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None, pk=None):
        if pk:
            try:
                if_exist = Recipe.objects.filter(id=pk)

                if if_exist:
                    Recipe.objects.filter(id=pk).update(is_active=False)
                    RecipeIngredient.objects.filter(recipe_id=pk).delete()
                    return Response({'error': '', 'error_code': '', 'data': 'Data has been Deleted'}, status=200)

                else:
                    return Response({'error': "Please insert valid ID", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)

            except Exception as e :
                return Response({'error': 'Please insert valid ID', 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
        else:
            return Response({'error': "No ID is given", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)


class SaveRecipeAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        recipe_list = []
        ingredient_id_list = []
        all_data_list = []
        recipe_sequence_list = []
        parts_id = []
        all_serializer_data = []
        try:
            data = (request.data)
            recipe_dict = dict()
            recipe_dict['name'] =  data['name']
            recipe_dict['recipe_type'] = data['recipe_type']
            recipe_list.append(recipe_dict)

            recipe_serializer = RecipeSerializer(
                context={'request': request}, data=recipe_dict)
            if recipe_serializer.is_valid():
                recipe_serializer.save()
                recipe_id = (recipe_serializer.data['id'])
            else:
                return Response({'error': recipe_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

            IngredientandParts_dict = dict()
            ingredient_id = data['ingredient']
            ingredient_id = ingredient_id.split(',')
            for ingredient in ingredient_id:
                ingredient_id_dict = dict()
                ingredient_id_dict['ingredient'] = data['ingredient']
                ingredient_id_dict['ingredient'] = ingredient
                ingredient_id_dict['recipe_id'] = recipe_id
                parts_id.append(ingredient_id_dict)

            ingredient_part = data['parts']
            ingredient_part = ingredient_part.split(',')
            for parts in ingredient_part:
                ingredient_parts_id_dict = dict()
                ingredient_parts_id_dict['parts'] = parts
                ingredient_parts_id_dict['recipe'] = recipe_id 
                parts_id.append(ingredient_parts_id_dict)
                IngredientandParts_dict['recipe'] = recipe_id
                IngredientandParts_dict['ingredient'] = ingredient_id_dict['ingredient']
                IngredientandParts_dict['parts'] = parts

                ingredient_id_serializer = RecipeIngredientSerializer(data = IngredientandParts_dict)
                if ingredient_id_serializer.is_valid():
                    ingredient_id_serializer.save() 
                else:
                    return Response({'error': ingredient_id_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

            recipe_sequence = data['sequence']
            recipe_sequence = recipe_sequence.split(',')
            for sequence_number in recipe_sequence:
                recipe_sequence_dict = dict()
                recipe_sequence_dict['sequence_number'] = sequence_number
                recipe_sequence_dict['recipe'] = recipe_id
                recipe_sequence_list.append(recipe_sequence_dict)

                recipe_sequence_serializer = RecipeSequenceSerializer(data = recipe_sequence_dict)
            
                if recipe_sequence_serializer.is_valid():
                    recipe_sequence_serializer.save()

                else:
                    RecipeIngredient.objects.filter(recipe_id=recipe_id).delete()
                    Recipe.objects.filter(id=recipe_id).delete()
                    return Response({'error': recipe_sequence_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)
            
            all_data_list.append(recipe_list)
            all_data_list.append(parts_id)
            all_data_list.append(recipe_sequence_list)
            return Response(
                    {'error': '', 'error_code': '', 'data': all_data_list}, status=200)

        except Exception as error:
            return Response(
                        {'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


