from django.urls import path
from inventory import views



app_name = "inventory"

urlpatterns = [
    path('create_inventory/', views.IngredientsInventoryAPI.as_view(), name='create_inventory'),
    path('all_inventory/', views.IngredientsInventoryListAPI.as_view(), name='all_inventory'),
    path('update_inventory/<int:pk>/', views.UpdateInventoryAPI.as_view(), name='update_inventory'),
]
