from django.db import models
from django.contrib.auth.models import User

class CustomerOrder(models.Model):
    recipe = models.ForeignKey('recipe.Recipe', on_delete = models.DO_NOTHING) #bleu de chanel
    order_volume = models.IntegerField() # 4500
    assigned_to = models.ForeignKey(User, on_delete = models.DO_NOTHING) #Iqbal
    production_place = models.ForeignKey("company.WorkStation", on_delete = models.DO_NOTHING) # Lab-4
    order_status = models.CharField(choices=(("p", "Pending"), ("c", "Completed"), ("ip", "In Process"), ("e", "Error"), ("ii", "Insufficient Ingredients"), ("c", "Created")), max_length=2, default="c")
    remarks = models.TextField(null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True, blank=True, related_name="order_added_by")
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True, blank=True,related_name="order_updated_by")

    class Meta:
        db_table = "customer_order"


class OrderSteps(models.Model):
    customer_order = models.ForeignKey(CustomerOrder, on_delete = models.DO_NOTHING)
    step_info = models.JSONField()
    step_number = models.PositiveIntegerField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    step_status = models.CharField(choices=(("p", "Pending"), ("ip", "In Process"), ("c", "Completed"), ("e", "Error")), max_length=2, default="p")

    class Meta:
        db_table = "order_steps"
