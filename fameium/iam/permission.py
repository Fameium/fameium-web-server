"""
Permission module for handling api permissions
"""
from rest_framework import permissions
from iam.models import Tenant


class TenantPermission(permissions.BasePermission):
    """
    Global tenant permission check
    """

    def has_permission(self, request, view):

        tenant_id = request.GET.get("tenant_id", None)
        tenant = Tenant.objects.filter(pk=tenant_id).first()
        if (
            tenant
            and request.user.is_authenticated
            and tenant in request.user.tenants.all()
        ):
            request.tenant = tenant
            return True
        else:
            return False
