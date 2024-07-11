from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from container.models import Container
from container.serializer import ContainerSerializer, ContainerListSerializer, EditContainerSerializer
from custom_permissions.user_permissions import IsAdmin

class ContainerAPI(APIView):
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        try:
            container_serializer = ContainerSerializer(
                context={'request': request}, data=request.data)
            if container_serializer.is_valid():
                container_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': container_serializer.data}, status=200)
            else:
                return Response({'error': container_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class ContainerListAPI(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):

        cantainer_list = Container.objects.filter(is_active=True).order_by('-id') 
        cantainer_serializer = ContainerListSerializer(cantainer_list, many=True)
        return Response({'error': '', 'error_code': '', 'data': cantainer_serializer.data}, status=200)


class EditContainerAPI(APIView):
    permission_classes = [IsAdmin]
    
    def put(self, request, format=None, pk=None):
        if pk:
            try:
                container_data = Container.objects.get(pk=pk)
                container_serializer = EditContainerSerializer(container_data, data=request.data, partial=True)
                if container_serializer.is_valid():
                    container_serializer.save()
                    return Response(
                        {'error': '', 'error_code': '', 'data':container_serializer.data}, status=200)
                else:
                    return Response({'error': container_serializer.errors, 'error_code': 'HS002', 'matched': 'N', 'data': {}}, status=400)

            except Exception as e :
                print(repr(e))
                return Response({'error': repr(e), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
        else:
            return Response({'error': "No Id is given", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)


class DeleteContainerAPI(APIView):
    permission_classes = [IsAdmin]

    def delete(self, request, format=None, pk=None):
        if pk:
            try:
                container_data = Container.objects.get(id=pk)
                container_data.is_active = False
                container_data.save()
                return Response({'error': '', 'error_code': '', 'data': 'Data Has Been Deleted'}, status=200)

            except Exception as e :
                print(repr(e))
                return Response({'error': 'Please Insert Valid ID', 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
        else:
            return Response({'error': "No Id is given", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)