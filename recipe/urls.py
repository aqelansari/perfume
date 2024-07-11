from django.urls import path
from recipe import views




app_name = "recipe"

urlpatterns = [
                path('create_recipe_type/', views.RecipeTypeAPI.as_view(), name='create_recipe_type'),
                path('recipe_type_list/', views.RecipeTypeListAPI.as_view(), name='recipe_type_list'),
                path('recipe_activity/', views.RecipeActivityAPI.as_view(), name='recipe_activity'),
                path('recipe_activity_list/', views.RecipeActivityListAPI.as_view(), name='recipe_activity_list'),
                path('recipe/', views.RecipeAPI.as_view(), name='recipe'),
                path('recipe_list/', views.RecipeListAPI.as_view(), name='recipe_list'),
                path('recipe_ingredient/', views.RecipeIngredientAPI.as_view(), name='recipe_ingredient'),
                path('recipe_ingredient_list/', views.RecipeIngredientListAPI.as_view(), name='recipe_ingredient_list'),
                path('recipe_activities/', views.RecipeActivitiesAPI.as_view(), name='recipe_activities'),
                path('recipe_activities_list/', views.RecipeActivitiesListAPI.as_view(), name='recipe_activities_list'),
                path('recipe_sequence/', views.RecipeSequenceAPI.as_view(), name='recipe_sequence'),
                path('recipe_sequence_list/', views.RecipeSequenceListAPI.as_view(), name='recipe_sequence_list'),
                path('ingredient_notes_search/', views.IngredientNotesSearchAPI.as_view(), name='ingredient_notes_search'),
                path('delete_recipe/<int:pk>/', views.DeleteRecipeAPI.as_view(), name='delete_recipe'),
                path('save_recipe/', views.SaveRecipeAPI.as_view(), name='save_recipe'),
    
    
]
