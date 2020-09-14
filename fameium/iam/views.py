"""
Module that handles the IAM related views
"""
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from iam.serializers import LoginSerializer


class LoginView(APIView):
    """
    API View that handles the login API
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        """
        Method that handles successfull post request
        """
        token, created = Token.objects.get_or_create(user=request.user)
        user_serializer = LoginSerializer(request.user)
        content = {"user": user_serializer.data, "token": token.key}
        return Response(content)
