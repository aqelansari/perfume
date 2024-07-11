from django.db import models
from django.contrib.auth.models import User

#Models For Inventory
class IngredientsInventory(models.Model):
    ingredient = models.ForeignKey('ingredient.Ingredient', on_delete = models.DO_NOTHING) #santalol
    quantity = models.IntegerField() #10
    per_unit_price = models.DecimalField(decimal_places=2,max_digits=10) #6504.85
    added_on = models.DateTimeField(null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name="inventory_added_by", null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True, blank=True, related_name="inventory_updated_by")

    class Meta:
        db_table = "ingredient_inventory"