from django.urls import path
from customer_order import views




app_name = "customer_order"

urlpatterns = [

        path('create_customer_order/', views.CustomerOrderAPI.as_view(), name='create_customer_order'),
        path('all_customerOrder/', views.AllCustomerOrderAPI.as_view(), name='all_customerOrder'),
        path('update_customer_order/<int:pk>/', views.UpdateCustomerOrderAPI.as_view(), name='update_customer_order'),
        path('order_steps/', views.OrderStepsAPI.as_view(), name='order_steps'),
        path('all_order_steps/', views.AllOrderStepsAPI.as_view(), name='all_order_steps'),

]
