"""
Module that handles IAM related url definitions
"""

from django.conf.urls import url

from iam.views import LoginView


urlpatterns = [url(r"^login/", LoginView.as_view(), name="login")]
