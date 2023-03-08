from rest_framework.permissions import BasePermission


class AllowOnlyAuthorUser(BasePermission):
    edit_methods = ('PUT', 'PATCH', 'DELETE')

    def has_object_permission(self, request, _view, obj) -> bool:
        if request.user == obj.author:
            return True
        return False


class AllowOnlyAuthorizedUsers(BasePermission):
    edit_methods = ('GET', 'POST')

    def has_permission(self, request, _view) -> bool:
        if request.user.is_authenticated:
            return True
        return False
