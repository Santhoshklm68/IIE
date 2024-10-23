from django.db import models


class EmployeeModel(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_age = models.IntegerField()
    # emp_email = models.EmailField(null=True, blank=True)
    designation = models.CharField(max_length=20)
    salary = models.IntegerField()
    d_o_b =  models.DateField()

    class Meta:
        db_table = "Employee"
