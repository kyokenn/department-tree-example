from django.contrib import admin

from .models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = 'name', 'parent'
    search_fields = 'name',


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'middle_name', 'last_name', 'job', 'employment_date',
        'salary', 'department')
    search_fields = 'first_name', 'middle_name', 'last_name'


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
