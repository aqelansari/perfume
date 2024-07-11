from django.shortcuts import render
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customer_order.serializer import CustomerOrderSerializer,OrderStepsSerializer,AllCustomerOrderSerializer,UpdateCustomerOrderSerializer,AllOrderStepsSerializer
from customer_order.models import CustomerOrder,OrderSteps

class CustomerOrderAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            customer_order_serializer =  CustomerOrderSerializer(context={'request': request}, data=request.data)
            if customer_order_serializer.is_valid():
                # customer_order_serializer.save()
                # print(customer_order_serializer)
                # data_dict = dict()
                data_dict = customer_order_serializer.data
                data_dict['added_by'] = request.user.id
                data_dict['added_on'] = datetime.now()
                CustomerOrder.objects.create(recipe_id =data_dict['recipe'], order_volume=data_dict['order_volume'],assigned_to_id = data_dict['assigned_to'],
                                            production_place_id=data_dict['production_place'],remarks = data_dict['remarks'],
                                            added_on=data_dict['added_on'],added_by_id=data_dict['added_by'])

                return Response({'error': '', 'error_code': '', 'data': data_dict}, status=200)
            else:
                return Response({'error': customer_order_serializer.errors, 'error_code': 'HS002', 'data': '' }, status=400)
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class AllCustomerOrderAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        price = {'price':123}
        ls = []
        all_customerOrder_serializer = CustomerOrder.objects.all().order_by('-id')
        res = AllCustomerOrderSerializer(all_customerOrder_serializer, many=True)
        for x in res.data:
            ls.append(x)
            ls.append(price)

        return Response({'error': '', 'error_code': '', 'data': ls}, status=200)


class UpdateCustomerOrderAPI(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None, pk=None):
        if pk:
            try:
                update_customer_order = CustomerOrder.objects.get(pk=pk)
                serializer = UpdateCustomerOrderSerializer(update_customer_order,data=request.data, partial=True)
                if serializer.is_valid():
                    data_dict = serializer.validated_data
                    data_dict['updated_on'] = datetime.now()
                    data_dict['updated_by'] = request.user
                    serializer.save()
                    return Response(
                        {'error': '', 'error_code': '', 'data':serializer.data}, status=200)
                else:
                    return Response({'error': serializer.errors, 'error_code': 'HS002', 'matched': 'N', 'data': {}}, status=400)
            except Exception as e :
                print(repr(e))
                return Response({'error': repr(e), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
        else:


            return Response({'error': "No Id is given", 'error_code': 'H005', 'matched': 'N', 'data': {}}, status=400)


class OrderStepsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            order_steps_serializer =  OrderStepsSerializer(context={'request': request}, data=request.data)
            if order_steps_serializer.is_valid():
                data_dict = order_steps_serializer.data
                data_dict['start_time'] = datetime.now()
                data_dict['end_time'] = datetime.now()
                OrderSteps.objects.create(step_info=data_dict['step_info'], customer_order_id=data_dict['customer_order'],
                                                    step_number=data_dict['step_number'],start_time=data_dict['start_time'],
                                                    end_time=data_dict['end_time'],step_status=data_dict['step_status'])

                return Response({'error': '', 'error_code': '', 'data': data_dict}, status=200)
            else:
                return Response({'error': order_steps_serializer.errors, 'error_code': 'HS002', 'data': '' }, status=400)
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class AllOrderStepsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_order_steps = OrderSteps.objects.all().order_by('-id')
        res = AllOrderStepsSerializer(all_order_steps, many=True)
        return Response({'error': '', 'error_code': '', 'data': res.data}, status=200)
