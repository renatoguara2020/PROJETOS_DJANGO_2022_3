from django.db import models


class Employees(models.Model):
    emp_id = models.AutoField.auto_created(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()
