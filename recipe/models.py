from django.db import models

class RecipeType(models.Model):
    name = models.CharField(max_length=50, unique=True) #Perfume
    state_of_matter = models.CharField(choices=(("s", "Solid"), ("l", "Liquid"), ("g", "Gas")), max_length=1)
    is_active = models.BooleanField() #true / false

    class Meta:
        db_table = "recipe_type"


class RecipeActivity(models.Model):
    name = models.CharField(max_length=50, unique=True) #Mixing
    is_active = models.BooleanField() #true / false

    class Meta:
        db_table = "recipe_activity"


class Recipe(models.Model):
    name = models.CharField(max_length=50, unique=True) #bleu de chanel
    recipe_type = models.ForeignKey(RecipeType, on_delete = models.DO_NOTHING) #Perfume
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "recipe"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.DO_NOTHING) #bleu de chanel
    ingredient = models.ForeignKey("ingredient.Ingredient", on_delete = models.DO_NOTHING) #santalol
    parts = models.PositiveIntegerField() #3

    class Meta:
        db_table = "recipe_ingredient"


class RecipeActivities(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.DO_NOTHING) #bleu de chanel
    activity = models.ForeignKey(RecipeActivity, on_delete = models.DO_NOTHING) #Mixing
    duration = models.DecimalField(decimal_places=2,max_digits=10) #10
    remarks = models.TextField() #do not stirr just leave the solution to dissolve

    class Meta:
        db_table = "recipe_activities"


class RecipeSequence(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.DO_NOTHING) #bleu de chanel
    activity = models.ForeignKey(RecipeActivities, on_delete = models.DO_NOTHING, null=True, blank=True) #Mixing
    ingredient = models.ForeignKey("ingredient.Ingredient", on_delete = models.DO_NOTHING, null=True, blank=True) #santalol
    sequence_number = models.PositiveIntegerField(unique=True) #1

    class Meta:
        db_table = "recipe_sequence"
