from email.policy import default
from django.db import models
from django.contrib.auth.models import User

USER_TYPE = [('AD', 'Admin'), ('LI', 'Lab Incharge'), ('SI', 'Shift Incharge'), ('WK', 'Worker')]

class Profile(models.Model):
    i_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPE,max_length=2,default='WK')
    profile_pic = models.CharField(null=True,blank = True,max_length=200)
    class Meta:
        db_table = 'profile'