"""
Middleware for handling tenant
"""

from django.http import JsonResponse
from django.urls import reverse


class TenantMiddleware:
    """
    Tenant handling middleware.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # For login request tenant verification is not needed
        if request.path == reverse("login"):
            return self.get_response(request)

        tenant_id = request.GET.get("tenant_id", None)
        if tenant_id is None:
            response = JsonResponse(
                {"detail": "Mising Required parameter 'tenant_id'"}, status=400
            )
        elif tenant_id is not None:
            try:
                int(tenant_id)
                response = self.get_response(request)
            except ValueError:
                response = JsonResponse(
                    {"detail": "Invalid value for 'tenant_id'"}, status=400
                )
        return response
