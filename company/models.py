from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=128) #Al Aziz Enterprises
    status = models.BooleanField(default=True)
    class Meta:
        db_table = "company"


class WorkStation(models.Model):
    company = models.ForeignKey(Company, on_delete = models.DO_NOTHING) #Al Aziz Enterprises
    name = models.CharField(max_length=128) #Lab-1
    production_capacity = models.PositiveIntegerField() #160 KG
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = "workstation"
        
        
        