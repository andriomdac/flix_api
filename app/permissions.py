from rest_framework.permissions import BasePermission


class GlobalDefaultPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD',]:
            method_name = 'view'
        elif request.method == 'POST':
            method_name = 'add'
        elif request.method in ['PUT', 'PATCH',]:
            method_name = 'change'
        elif request.method == 'DELETE':
            method_name = 'delete'
        else:
            return False

        app_name = view.queryset.model._meta.app_label
        model_name = view.queryset.model._meta.model_name

        formated_string = f'{app_name}.{method_name}_{model_name}'

        return request.user.has_perm(formated_string)
