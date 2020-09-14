"""
Handles API views related to productivity
"""

from iam.viewsets import ModelTenantViewSet

from rest_framework.views import APIView
from rest_framework.response import Response

from productivity.models import Project, Idea, Sponsership, Template
from productivity.serializers import (
    ProjectSerializer,
    IdeaSerializer,
    SponsershipSerializer,
    TemplateSerializer,
)


class ProjectViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing projects.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class IdeaViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing ideas.
    """

    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class SponsershipViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing sponserships.
    """

    queryset = Sponsership.objects.all()
    serializer_class = SponsershipSerializer


class TemplateViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing Templates.
    """

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class ProductivityView(APIView):
    """
    Api view for handling productivity main page
    """

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(tenant=request.tenant)
        ideas = Idea.objects.filter(tenant=request.tenant)
        sponserships = Sponsership.objects.filter(tenant=request.tenant)

        context = {
            "request": request,
        }

        projects_serializer = ProjectSerializer(
            projects, many=True, context=context, fields=("id", "name", "status")
        )
        ideas_serializer = IdeaSerializer(
            ideas, many=True, context=context, fields=("id", "name")
        )
        sponserships_serializer = SponsershipSerializer(
            sponserships, many=True, context=context, fields=("id", "name")
        )

        response = {
            "projects": projects_serializer.data,
            "ideas": ideas_serializer.data,
            "sponserships": sponserships_serializer.data,
        }

        return Response(response)
