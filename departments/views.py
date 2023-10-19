from django.http import Http404
from django.views.generic import TemplateView

from .models import Department, Employee


class DepartmentView(TemplateView):
    template_name = 'departments/department.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        objs_by_id = {}
        tree = []
        for department in Department.objects.order_by('parent_id'):
            obj = {
                'id': department.id,
                'name': department.name,
                'children': [],
            }
            objs_by_id[department.id] = obj

            if department.parent:
                obj['parent_id'] = department.parent_id
                parent_obj = objs_by_id[department.parent_id]
                parent_obj['children'].append(obj)
            else:
                tree.append(obj)

        context['department'] = {'children': tree}

        department_id = kwargs.get('id')
        if department_id:
            if department_id in objs_by_id:
                context['id'] = department_id

                page = 1
                page_size = 20
                if self.request.GET.get('page', '').isdigit():
                    page = max(1, int(self.request.GET.get('page')))

                employees = Employee.objects.filter(department_id=department_id)
                context['employees'] = employees[(page - 1) * page_size:page * page_size]

                context['page'] = page
                if page > 1:
                    context['previous'] = f'?page={page-1}'
                if page < employees.count() / page_size:
                    context['next'] = f'?page={page+1}'

                while department_id:
                    obj = objs_by_id[department_id]
                    obj['is_active'] = True
                    department_id = obj.get('parent_id')
            else:
                raise Http404

        return context
