
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from company.models import Company, WorkStation
from company.serializer import AllCompanySerializer, AllWorkstationSerializer, CompanySerializer, WorkstationSerializer
from custom_permissions.user_permissions import IsAdmin


class CompanyAPI(APIView):
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        try:
            company_serializer = CompanySerializer(
                context={'request': request}, data=request.data)
            if company_serializer.is_valid():
                company_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': company_serializer.data}, status=200)
            else:
                return Response({'error': company_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class CompanyListAPI(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):

        all_companies = Company.objects.filter(status=True).order_by('-id')
        res = AllCompanySerializer(all_companies, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)


class WorkStationAPI(APIView):
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        try:
            workstation_serializer = WorkstationSerializer(
                context={'request': request}, data=request.data)
            if workstation_serializer.is_valid():
                workstation_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': workstation_serializer.data}, status=200)
            else:
                return Response({'error': workstation_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class WorkStationListAPI(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        
        try:

            all_workstations = WorkStation.objects.filter(
                status=True).order_by('-id')
            res = AllWorkstationSerializer(all_workstations, many=True)
            return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)
    
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)
