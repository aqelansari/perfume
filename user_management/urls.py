from django.urls import path

import user_management.views as views


app_name = "user_management"

urlpatterns = [
    path('create_app_user/', views.AppUser.as_view(), name='create-app-user'),
    path('get_user/', views.AppUserDetail.as_view(), name='create-app-user'),
    path('get_users_list/', views.ListUsersAPI.as_view(), name='get-users-list'),
    path('change_password/', views.ChangePassword.as_view(), name='change-password'),
    
]
