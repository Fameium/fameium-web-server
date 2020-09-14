"""
Module that handles IAM related url definitions
"""

from django.conf.urls import url

from productivity.views import (
    ProjectViewSet,
    IdeaViewSet,
    SponsershipViewSet,
    ProductivityView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"ideas", IdeaViewSet, basename="idea")
router.register(r"sponserships", SponsershipViewSet, basename="sponsership")

api_urls = [url(r"^productivity/", ProductivityView.as_view(), name="productivity")]


urlpatterns = router.urls + api_urls
