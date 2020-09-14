"""
Handles serializers for productivity module
"""
from rest_framework import serializers
from productivity.models import Project, Idea, Sponsership

from django.db.utils import IntegrityError


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ProjectSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "motes",
            "created_time",
            "start_date",
            "end_date",
            "status",
            "sponsorships",
            "script",
            "last_edited_time",
        ]
        read_only_fields = ["id", "created_time", "last_edited_time", "sponsorships"]


class IdeaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Idea
        fields = [
            "id",
            "name",
            "description",
            "motes",
            "created_time",
            "last_edited_time",
        ]
        read_only_fields = ["id", "created_time", "last_edited_time"]


class SponsershipSerializer(DynamicFieldsModelSerializer):

    projects = serializers.SerializerMethodField()

    class Meta:
        model = Sponsership
        fields = [
            "id",
            "name",
            "description",
            "motes",
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
        read_only_fields = ["id", "created_time", "last_edited_time", "products"]

    def get_projects(self, obj):
        products = (
            obj.project_set.all()
        )  # will return project query set associate with this category
        response = ProjectSerializer(products, many=True).data
        return response


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = [
            "id",
            "name",
            "description",
            "motes",
            "content",
            "created_time",
            "last_edited_time",
        ]
        read_only_fields = ["id", "created_time", "last_edited_time"]
