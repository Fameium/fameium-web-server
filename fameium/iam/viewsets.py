"""
Module for handling custom viewsets
"""

from rest_framework import viewsets


class ModelTenantViewSet(viewsets.ModelViewSet):
    """
    Abstract ModelViewSet with tenant handling
    """

    extra_create_params = {}
    extra_update_params = {}
    ordering = ["-last_edited_time"]

    def get_queryset(self):
        """
        This method will return filtered queryset based
        on tenant for the currently authenticated user.
        """
        return self.queryset.filter(tenant=self._get_tenant())

    def perform_create(self, serializer):
        """
        Custom serializer create function with tenant parameter
        """
        serializer.save(tenant=self._get_tenant(), **self._get_extra_create_params())

    def perform_update(self, serializer):
        """
        Custom serializer update function with tenant parameter
        """
        serializer.save(user=self._get_tenant(), **self._get_extra_update_params())

    def _get_tenant(self):
        """
        Return the current request tenant
        """
        return self.request.tenant

    def _get_extra_create_params(self):
        """
        Method to get extra create parameters for serializer
        """
        return self.extra_create_params

    def _get_extra_update_params(self):
        """
        Method to get extra update parameters for serializer
        """
        return self.extra_update_params
