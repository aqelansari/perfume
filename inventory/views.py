from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ingredient.models import Ingredient
from inventory.serializer import IngredientsInventorySerializer,AllIngredientInventorySerializer,UpdateInventoryAPISerializer
from datetime import datetime
from inventory.models import IngredientsInventory
from container.models import Container
from custom_permissions.user_permissions import IsAdmin


class IngredientsInventoryAPI(APIView):
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        try:
            inventory_serializer = IngredientsInventorySerializer(
                context={'request': request}, data=request.data)
            if inventory_serializer.is_valid():
                data_dict = inventory_serializer.data
                data_dict['added_by'] = request.user.id
                data_dict['added_on'] = datetime.now()
                IngredientsInventory.objects.create(ingredient_id =data_dict['ingredient'], quantity=data_dict['quantity'],per_unit_price = data_dict['per_unit_price'],
                added_by_id=data_dict['added_by'],added_on = data_dict['added_on'])
                
                return Response(
                    {'error': '', 'error_code': '', 'data': data_dict}, status=200)
            else:
                return Response({'error': inventory_serializer.errors, 'error_code': 'HS002', 'data': ''}, status=400)

        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': ''}, status=400)


class IngredientsInventoryListAPI(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        inventory_list = []
        all_data_list = []
        all_inventory = IngredientsInventory.objects.all().order_by('-id')
        for a in all_inventory:
            inventory_id_dict = dict()
            ingredient_id = a.ingredient.id
            inventory_id = a.id
            ingredient_name = a.ingredient.name
            quantity = a.quantity
            per_unit_price = a.per_unit_price
            inventory_id_dict['id'] = inventory_id
            inventory_id_dict['ingredient_id'] = ingredient_id
            inventory_id_dict['ingredient_name'] = ingredient_name
            inventory_id_dict['quantity'] = quantity
            inventory_id_dict['per_unit_price'] = per_unit_price
            inventory_list.append(inventory_id_dict)
            container_id = Container.objects.filter(ingredient_id = ingredient_id)
            for container in container_id:
                c_id = container.name
                container_volume = container.volume
                inventory_id_dict['container'] = c_id
                inventory_id_dict['container_volume'] = container_volume
            all_data_list.append(inventory_id_dict)
            #res = AllIngredientInventorySerializer(all_data_list, many=True)
        return Response({'error': '', 'error_code': '', 'data': all_data_list}, status=200)


class UpdateInventoryAPI(APIView):
    permission_classes = [IsAdmin]  

    def put(self, request, format=None, pk=None):
        if pk:
            try:
                IngredientsInventory_data= IngredientsInventory.objects.get(pk=pk)
                serializer = UpdateInventoryAPISerializer(IngredientsInventory_data,data=request.data, partial=True)
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


