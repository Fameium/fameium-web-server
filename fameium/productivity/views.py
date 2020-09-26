"""
Handles API views related to productivity
"""

from iam.viewsets import ModelTenantViewSet

from rest_framework.views import APIView
from rest_framework.response import Response

from productivity.models import Project, Idea, Sponsorship, Template
from productivity.serializers import (
    ProjectSerializer,
    IdeaSerializer,
    SponsorshipSerializer,
    TemplateSerializer,
)


class ProjectViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing projects.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    ordering_fields = fields = [
        "id",
        "name",
        "description",
        "notes",
        "created_time",
        "start_date",
        "end_date",
        "status",
        "sponsorships",
        "script",
        "last_edited_time",
    ]


class IdeaViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing ideas.
    """

    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    ordering_fields = [
        "id",
        "name",
        "description",
        "notes",
        "created_time",
        "last_edited_time",
    ]


class SponsorshipViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing sponsorships.
    """

    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    ordering_fields = [
        "id",
        "name",
        "description",
        "notes",
        "sponsorship_type",
        "no_of_videos",
        "start_date",
        "end_date",
        "total_amount",
        "agreement",
        "projects",
        "created_time",
        "last_edited_time",
    ]


class TemplateViewSet(ModelTenantViewSet):
    """
    ViewSet for viewing and editing Templates.
    """

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    ordering_fields = [
        "id",
        "name",
        "description",
        "notes",
        "content",
        "created_time",
        "last_edited_time",
    ]


class ProductivityView(APIView):
    """
    Api view for handling productivity main page
    """

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(tenant=request.tenant).order_by(
            "-last_edited_time"
        )
        ideas = Idea.objects.filter(tenant=request.tenant).order_by("-last_edited_time")
        sponsorships = Sponsorship.objects.filter(tenant=request.tenant).order_by(
            "-last_edited_time"
        )

        context = {
            "request": request,
        }

        projects_serializer = ProjectSerializer(
            projects, many=True, context=context, fields=("id", "name", "status")
        )
        ideas_serializer = IdeaSerializer(
            ideas, many=True, context=context, fields=("id", "name")
        )
        sponsorships_serializer = SponsorshipSerializer(
            sponsorships, many=True, context=context, fields=("id", "name")
        )

        response = {
            "projects": projects_serializer.data,
            "ideas": ideas_serializer.data,
            "sponsorships": sponsorships_serializer.data,
        }

        return Response(response)
