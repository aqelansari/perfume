from django.urls import path
from container import views




app_name = "container"

urlpatterns = [

        path('create_container/', views.ContainerAPI.as_view(), name='create_container'),
        path('all_container/', views.ContainerListAPI.as_view(), name='all_container'),
        path('edit_container/<int:pk>/', views.EditContainerAPI.as_view(), name='edit_container'),
        path('delete_container/<int:pk>/', views.DeleteContainerAPI.as_view(), name='delete_container'),

]