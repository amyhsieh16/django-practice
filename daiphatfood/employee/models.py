from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    employee_no=models.IntegerField()
    employee_name=models.CharField(max_length=64)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name
    