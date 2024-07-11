from django.urls import path
from company import views


app_name = "company"

urlpatterns = [
    path('create_company/', views.CompanyAPI.as_view(), name='create-company'),
    path('all_company/', views.CompanyListAPI.as_view(), name='all-company'),
    path('create_workstation/', views.WorkStationAPI.as_view(), name='create-workstation'),
    path('all_workstation/', views.WorkStationListAPI.as_view(), name='all-workstation'),
    
]
