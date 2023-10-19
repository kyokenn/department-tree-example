from django.db import models


class Department(models.Model):
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField('Name', max_length=256)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField('First Name', max_length=1024)
    middle_name = models.CharField('Middle Name', max_length=1024)
    last_name = models.CharField('Last Name', max_length=1024)
    job = models.CharField('Job title', max_length=1024)
    employment_date = models.DateField('Employment Date')
    salary = models.PositiveIntegerField('Salary')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
