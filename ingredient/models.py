from django.db import models

class IngredientType(models.Model):
    type_name = models.CharField(max_length=128, unique=True) #powder
    recipe_order = models.PositiveIntegerField(unique=True) # 1
    is_active = models.BooleanField() #true / false

    class Meta:
        db_table = "ingredient_type"


class IngredientApp(models.Model):
    application_name = models.CharField(max_length=128, unique=True) #confectionary
    is_active = models.BooleanField() #true / false

    class Meta:
        db_table = "ingredient_app"


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True) #santalol
    ingredient_type = models.ForeignKey(IngredientType, on_delete = models.DO_NOTHING) #powder
    threshold_limit = models.DecimalField(decimal_places=2,max_digits=10) #95.8
    ingredient_code = models.CharField(max_length=128, unique=True) #PWD-SAN-9281
    remarks = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "ingredient"


class IngredientApplications(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete = models.DO_NOTHING) #santalol
    ingredient_application = models.ForeignKey(IngredientApp, on_delete = models.DO_NOTHING) #confectionary
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "ingredient_applications"


class IngredientNotes(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete = models.DO_NOTHING) #santalol
    notes = models.CharField(max_length=50) #citrus
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "ingredient_notes"


class IngredientIncompatible(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete = models.DO_NOTHING, related_name="ingredient_incompatible_ingredient") #santalol
    incompatible = models.ForeignKey(Ingredient, on_delete = models.DO_NOTHING, related_name="ingredient_incompatible_incompatible") #benzene
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "ingredient_incompatibile"



