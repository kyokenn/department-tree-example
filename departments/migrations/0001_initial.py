# Generated by Django 4.2.6 on 2023-10-17 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='departments.department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1024, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=1024, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=1024, verbose_name='Last Name')),
                ('job', models.CharField(max_length=1024, verbose_name='Job title')),
                ('employment_date', models.DateField(verbose_name='Employment Date')),
                ('salary', models.PositiveIntegerField(verbose_name='Salary')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
            ],
        ),
    ]
