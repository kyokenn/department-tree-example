# Generated by Django 4.2.6 on 2023-10-17 18:40
import datetime
import random

from django.db import migrations

FIRST_NAMES = [
    'James', 'John', 'Robert', 'Michael', 'William',
    'Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth',
]
MIDDLE_NAMES = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller',
    'Davis', 'Garcia', 'Rodriguez', 'Wilson','Martinez',
]
JOB_TITLES = [
    'Manager', 'Analyst', 'Scientist', 'Engineer', 'Architect',
    'Developer', 'Administrator',
]


def forward(apps, schema_editor):
    now = datetime.datetime.now()
    Employee = apps.get_model('departments', 'Employee')
    Department = apps.get_model('departments', 'Department')
    for department in Department.objects.all():
        employees = []
        for _ in range(random.randint(500, 2000)):
            dt = datetime.timedelta(days=random.randint(7, 365 * 5))
            employee = Employee(
                first_name=random.choice(FIRST_NAMES),
                middle_name=random.choice(MIDDLE_NAMES),
                last_name=random.choice(FIRST_NAMES),
                job=random.choice(JOB_TITLES),
                employment_date=now - dt,
                salary=random.randint(15, 300) * 1000,
                department=department)
            employees.append(employee)
        Employee.objects.bulk_create(employees)


def backward(apps, schema_editor):
    Employee = apps.get_model('departments', 'Employee')
    Employee.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20231017_1327'),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]