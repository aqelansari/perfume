from django.urls import path
from ingredient import views




app_name = "ingredient"

urlpatterns = [
    
    path('create_ingredient_type/', views.IngredientTypeAPI.as_view(), name='create-ingredient-type'),
    path('all_ingredient_type/', views.IngredientTypeListAPI.as_view(), name='all-ingredient-type'),
    path('create_ingredient_app/', views.IngredientAppAPI.as_view(), name='create-ingredient-app'),
    path('all_ingredient_app/', views.IngredientAppListAPI.as_view(), name='all-ingredient-app'),
    path('create_ingredient/', views.IngredientAPI.as_view(), name='create-ingredient'),
    path('all_ingredient/', views.IngredientListAPI.as_view(), name='all-ingredient'),
    path('create_ingredient_applications/', views.IngredientApplicationsAPI.as_view(), name='create-ingredient-applications'),
    path('all_ingredient_applications/', views.IngredientApplicationsListAPI.as_view(), name='all-ingredient-applications'),
    path('create_ingredient_notes/', views.IngredientNoteAPI.as_view(), name='create-ingredient-app'),
    path('all_ingredient_note/', views.IngredientNotesListAPI.as_view(), name='all-ingredient-app'),
    path('create_ingredient_incompatible/', views.IngredientIncompatibleAPI.as_view(), name='create-ingredient-incompatible'),
    path('all_ingredient_incompatible/', views.IngredientIncompatibleListAPI.as_view(), name='all-ingredient-incompatible'),
    path('delete_ingredient/<int:pk>/', views.DeleteIngredientAPI.as_view(), name='delete_ingredient'),
    
]
