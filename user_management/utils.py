from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    # for login error
    if response is None:
        return Response(
            {'error': 'Invalid Credentials', 'error_code': 'HI005', 'message': '', 'data': {}},
            status=400)
    if response is not None:
        response.data['status_code'] = response.status_code
    return Response(
        {'error': ['The signature is not verified'], 'error_code': 'HI005', 'message': '', 'data': {}},
        status=401)