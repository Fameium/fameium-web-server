"""
Module for handling IAM related API serializers.
"""

from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["tenants", "username", "first_name", "last_name", "email"]
        depth = 1
