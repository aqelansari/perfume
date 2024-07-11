from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ingredient.serializer import AllIngredientSerializer, IngredientApplicationsListSerializer, IngredientIncompatibleListSerializer,\
    IngredientIncompatibleSerializer, IngredientNoteSerializer, IngredientNotesListSerializer, IngredientSerializer, IngredientTypeSerializer,\
    AllIngredientTypeSerializer,AllIngredientAppSerializer,IngredientAppSerializer,IngredientApplicationsSerializer
from ingredient.models import Ingredient, IngredientApplications, IngredientIncompatible, IngredientNotes, IngredientType,IngredientApp
import pdb

class IngredientTypeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            ingredient_serializer = IngredientTypeSerializer(
                context={'request': request}, data=request.data)
            if ingredient_serializer.is_valid():
                ingredient_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': ingredient_serializer.data}, status=200)
            else:
                return Response({'error': ingredient_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class IngredientTypeListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_ingredient_type = IngredientType.objects.filter(
            is_active=True).order_by('-id')
        res = AllIngredientTypeSerializer(all_ingredient_type, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)



class IngredientAppAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            ingredient_app_serializer = IngredientAppSerializer(
                context={'request': request}, data=request.data)
            if ingredient_app_serializer.is_valid():
                ingredient_app_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': ingredient_app_serializer.data}, status=200)
            else:
                return Response({'error': ingredient_app_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class IngredientAppListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_ingredient_apps = IngredientApp.objects.filter(
            is_active=True).order_by('-id')
        res = AllIngredientAppSerializer(all_ingredient_apps, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)



class IngredientAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        notes_list = []
        applications_list = []
        incompatibal_list = []
        ingredient_model_data = []
        all_data_list = []
        try:
            all_data = (request.data)
            ingredient_notes = all_data['notes']
            ingredient_notes = ingredient_notes.split(',')
            ingredient_notes = list(set(ingredient_notes))
            ingredient_data = dict()
            ingredient_data['name'] = all_data['name']
            ingredient_data['threshold_limit'] = all_data['threshold_limit']
            ingredient_data['ingredient_code'] = all_data['ingredient_code']
            ingredient_data['ingredient_type'] = all_data['ingredient_type']
            ingredient_model_data.append(ingredient_data)

            ingredient_serializer = IngredientSerializer(
                context={'request': request}, data=ingredient_data)
            if ingredient_serializer.is_valid():
                ingredient_serializer.save()
                ingredient_id = ingredient_serializer.data['id']

            else:
                return Response({'error': ingredient_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

            for notes in ingredient_notes:
                ingredient_notes_data = dict()
                ingredient_notes_data['ingredient'] = ingredient_id
                ingredient_notes_data['name'] = all_data['name']
                ingredient_notes_data['threshold_limit'] = all_data['threshold_limit']
                ingredient_notes_data['ingredient_code'] = all_data['ingredient_code']
                ingredient_notes_data['ingredient_type'] = all_data['ingredient_type']
                ingredient_notes_data['notes'] = notes
                notes_serializer = IngredientNoteSerializer(data = ingredient_notes_data)

                if notes_serializer.is_valid():
                    notes_serializer.save()
                    notes_list.append(ingredient_notes_data)

                else:
                    return Response({'error': notes_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)


            ingredient_application = all_data['ingredient_application']
            ingredient_application = ingredient_application.split(',')
            for application in ingredient_application:
                ingredient_applications_data = dict()
                ingredient_applications_data['ingredient'] = ingredient_id
                ingredient_applications_data['name'] = all_data['name']
                ingredient_applications_data['threshold_limit'] = all_data['threshold_limit']
                ingredient_applications_data['ingredient_code'] = all_data['ingredient_code']
                ingredient_applications_data['ingredient_type'] = all_data['ingredient_type']
                ingredient_applications_data['ingredient_application'] = application
                applications_serializer = IngredientApplicationsSerializer(data = ingredient_applications_data)
            
                if applications_serializer.is_valid():
                    applications_serializer.save()
                    applications_list.append(ingredient_applications_data)

                else:
                    IngredientNotes.objects.filter(ingredient_id=ingredient_id).delete()
                    Ingredient.objects.filter(id=ingredient_id).delete()
                    return Response({'error': applications_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

            incompatible = all_data['incompatible']
            incompatible = incompatible.split(',')
            for incompatibal in incompatible:
                ingredient_incompatibal_data = dict()
                ingredient_incompatibal_data['ingredient'] = ingredient_id
                ingredient_incompatibal_data['name'] = all_data['name']
                ingredient_incompatibal_data['threshold_limit'] = all_data['threshold_limit']
                ingredient_incompatibal_data['ingredient_code'] = all_data['ingredient_code']
                ingredient_incompatibal_data['ingredient_type'] = all_data['ingredient_type']
                ingredient_incompatibal_data['incompatible'] = incompatibal
                incompatibal_serializer = IngredientIncompatibleSerializer(data = ingredient_incompatibal_data)
                if incompatibal_serializer.is_valid():
                    incompatibal_serializer.save()
                    incompatibal_list.append(ingredient_incompatibal_data)

                else:
                    IngredientApplications.objects.filter(ingredient_id=ingredient_id).delete()
                    IngredientNotes.objects.filter(ingredient_id=ingredient_id).delete()
                    Ingredient.objects.filter(id=ingredient_id).delete()
                    return Response({'error': incompatibal_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)
            all_data_list.append(notes_list)
            all_data_list.append(applications_list)
            all_data_list.append(incompatibal_list)

            return Response(
                {'error': '', 'error_code': '', 'data': all_data_list}, status=200)


        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)
            

class IngredientListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_ingredients = Ingredient.objects.filter(is_active=True).order_by('-id')   
        res = AllIngredientSerializer(all_ingredients, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)



class IngredientApplicationsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data_list = []
        try:
            api_data = (request.data)
            ingredient = api_data['ingredient']
            ingredient_application = api_data['ingredient_application']
            ingredient_application = ingredient_application.split(',')
            for application in ingredient_application:
                app_dict = dict()
                app_dict['ingredient'] = ingredient
                app_dict['ingredient_application'] = application 
                ingredient_applications_serializer = IngredientApplicationsSerializer(
                context={'request': request}, data=app_dict)
                if ingredient_applications_serializer.is_valid():
                    ingredient_applications_serializer.save()
                    data_list.append(app_dict)
                else:
                    return Response({'error': ingredient_applications_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)
            return Response(
                {'error': '', 'error_code': '', 'data': data_list}, status=200)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class IngredientApplicationsListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        all_ingredient_app = IngredientApplications.objects.all().order_by('-id')
        res = IngredientApplicationsListSerializer(all_ingredient_app, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)



class IngredientNoteAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data_list = []
        try:
            ingredient_note_serializer = (request.data)
            notes = ingredient_note_serializer['notes']
            ingredient = ingredient_note_serializer['ingredient']
            notes = notes.split(",")
            for note in notes:
                note_dict = dict()
                note_dict['ingredient'] = ingredient
                note_dict['notes'] = note
                serializer = IngredientNoteSerializer(data = note_dict)
                if serializer.is_valid():
                    serializer.save()
                    data_list.append(serializer.initial_data)
                else:
                    return Response({'error': serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)
            return Response(
                {'error': '', 'error_code': '', 'data': data_list}, status=200)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class IngredientNotesListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        all_ingredient_notes = IngredientNotes.objects.all().order_by('-id')
        res = IngredientNotesListSerializer(all_ingredient_notes, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)



class IngredientIncompatibleAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data_list = []
        try:
            if request.data['ingredient'] == request.data['incompatible']:
                return Response('This Incompatible is not Allow')
            else:
                api_data = (request.data)
                ingredient = api_data['ingredient']
                incompatible = api_data['incompatible']
                incompatible = incompatible.split(',')
                for comppatible in incompatible:
                    comp_dict = dict()
                    comp_dict['ingredient'] = ingredient
                    comp_dict['incompatible'] = comppatible
                    ingredient_applications_serializer = IngredientIncompatibleSerializer(
                    context={'request': request}, data=comp_dict)
                    if ingredient_applications_serializer.is_valid():
                        ingredient_applications_serializer.save()
                        data_list.append(comp_dict)
                    else:
                        return Response({'error': ingredient_applications_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

                return Response(
                        {'error': '', 'error_code': '', 'data': data_list}, status=200)


        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class IngredientIncompatibleListAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        all_ingredient_incompatible = IngredientIncompatible.objects.all().order_by('-id')
        res = IngredientIncompatibleListSerializer(all_ingredient_incompatible, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)


class DeleteIngredientAPI(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None, pk=None):
        if pk:
            try:
                if_exist = Ingredient.objects.filter(id=pk)
                if if_exist:
                    IngredientApplications.objects.filter(ingredient_id=pk).update(is_active=False)
                    IngredientNotes.objects.filter(ingredient_id=pk).update(is_active=False)
                    IngredientIncompatible.objects.filter(ingredient_id=pk).update(is_active=False)
                    Ingredient.objects.filter(id=pk).update(is_active=False)

                    return Response({'error': '', 'error_code': '', 'data': 'Data Has Been Deleted'}, status=200)
                else:
                    return Response({'error': "Please Insert Valid ID", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)

            except Exception as e :
                return Response({'error': 'Please Insert Valid ID', 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
        else:
            return Response({'error': "No Id is given", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)