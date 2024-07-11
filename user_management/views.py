from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken
from user_management.models import Profile
from user_management.serializers import AllUsersSerializer, AppUserSerializer, ChangePasswordSerializer, GetUserSerializer, AllUsersPicsSerializer
from django.contrib.auth.models import User
from custom_permissions.user_permissions import IsAdmin


class CustomAuthLogin(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        valid_data = VerifyJSONWebTokenSerializer().validate(response.data)
        user = valid_data['user']
        response.data['username'] = user.username
        response.data['first_name'] = user.first_name
        response.data['last_name'] = user.last_name
        response.data['user_id'] = user.id

        return Response(
                        {'error': '', 'error_code': '', 'data': response.data}, status=200)
        
        
class AppUserDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try: 
            data=request.data
            if 'username' in data:
                username = str(data['username'])
                if username.isdigit():
                    if len(username) == 5:
                        exist = User.objects.filter(username=username).exists()
                        if exist :
                            user_obj = User.objects.get(username=username)
                            profile_pic = Profile.objects.get(i_user=user_obj).profile_pic
                            response_data = dict()
                            response_data['username'] = user_obj.username
                            response_data['first_name'] = user_obj.first_name
                            response_data['last_name'] = user_obj.last_name
                            response_data['profile_pic'] = profile_pic
                            response_data['user_id'] = user_obj.id
                            return Response(
                            {'error': '', 'error_code': '', 'data': response_data}, status=200)
                        return Response(
                        {'error': '', 'error_code': '', 'data': 'No Employee ID found'}, status=400)
                        
                    else:
                        return Response(
                        {'error': '', 'error_code': '', 'data': 'Please enter 5 digit Employee ID'}, status=400)
                else:
                    return Response(
                        {'error': 'Please enter Numeratic Employee ID only', 'error_code': 'HD402', 'data': {}}, status=402)
            else:
                return Response({'error': 'No Employee ID Found', 'error_code': 'H404', 'data':{}}, status=404)
    
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)

class AppUser(APIView):

    def post(self, request, *args, **kwargs):
        try:
            
            user_serializer = AppUserSerializer(context={'request': request}, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'data': user_serializer.data}, status=200)
            else:
                return Response({'error': user_serializer.errors, 'error_code': 'HS002', 'data':''}, status=400)
        
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class ListUsersAPI(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        all_users = Profile.objects.filter(i_user__is_active=True,i_user__is_superuser = False).order_by('-id')
        res = AllUsersPicsSerializer(all_users, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            change_pass_serializer = ChangePasswordSerializer(data=request.data)
            if change_pass_serializer.is_valid():
                change_pass_serializer.save()
                return Response(
                    {'error': '', 'error_code': '', 'change_password_data': change_pass_serializer.data}, status=200)
            else:
                return Response({'error': change_pass_serializer.errors.keys(), 'error_code': 'HS002', 'change_password_data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)