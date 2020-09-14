"""
Handles the IAM related model definitions
"""

from django.db import models

from django.contrib.auth.models import (
    AbstractUser,
)  # we will be extending the AbstractUser model as our user model.


class Tenant(models.Model):
    """
    The tenant tableis the core of the multi tenancy
    in the entire fameium framework.
    It hold detaild about the tenant.
    All other tables should have a foreign key relation
    with the Tenant table if they store tenant specific data.
    the fk relation should be non nullable at db level.
    That means every table entry for all other tables should have a tenant
    """

    portal_name = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    last_edited_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"

    def __str__(self):
        return self.portal_name or self.id


class TenantModel(models.Model):
    """
    Abstract class that must be inherited by all the tables in all models,
    if they deal with tenant specific data
    So tenant column will be bydefault created for all tables if they inherit this class.
    """

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_edited_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    """
    The auth usrer model in fameium.
    We wont be using djangos default model as we need to support multi tenancy
    """

    phone = models.CharField(max_length=50)
    isd_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=5)
    created_time = models.DateTimeField(auto_now_add=True)
    last_edited_time = models.DateTimeField(auto_now=True)
    tenants = models.ManyToManyField(
        Tenant,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username or self.id
