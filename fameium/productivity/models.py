"""
Handles productivity related database models.
"""
from django.db import models
from iam.models import TenantModel


class AbstractProductivityModel(TenantModel):
    """
    Abstract model for  common fields in productivity
    """

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1500, blank=True)
    notes = models.CharField(max_length=1500, blank=True)

    class Meta:
        abstract = True


class Sponsorship(AbstractProductivityModel):
    """
    Database model for  Sponsorship details.
    """

    class SponsorshipType(models.IntegerChoices):
        """
        Status choice for the sponsorship_type.
        """

        DEDICATED = 0
        SHOUTOUT = 1

    sponsorship_type = models.IntegerField(
        choices=SponsorshipType.choices, default=SponsorshipType.DEDICATED
    )
    no_of_videos = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    total_amount = models.PositiveIntegerField(blank=True, null=True)
    agreement = models.TextField(max_length=2500, blank=True)


class Project(AbstractProductivityModel):
    """
    Database model for handling projects
    Extends from AbstractProjectIdea
    """

    class Status(models.IntegerChoices):
        """
        Status choice for the project.
        """

        TODO = 0
        PLANNING = 1
        SCRIPTING = 2
        PRODUCTION = 3
        EDITING = 4
        COMPLETED = 5
        PUBLISHED = 6

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.TODO)
    sponsorships = models.ManyToManyField(
        Sponsorship,
        null=True,
        blank=True,
    )
    script = models.TextField(max_length=2500, blank=True)


class Idea(AbstractProductivityModel):
    """
    Database model for handling Idea
    """

    pass


class Template(AbstractProductivityModel):
    """
    Database model for handlng script templates
    """

    content = models.CharField(max_length=2500, blank=True)
