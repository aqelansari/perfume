from django.db import models

class Container(models.Model):
    ingredient = models.OneToOneField('ingredient.Ingredient', on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=128, unique=True)
    volume = models.PositiveIntegerField()
    physical_location = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'container' 

