from rest_framework import permissions


class Permission(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return request.user.has_perm('link.change_link')


DjangoModelPermissions = permissions.DjangoModelPermissions
AllowAny = permissions.DjangoModelPermissions
