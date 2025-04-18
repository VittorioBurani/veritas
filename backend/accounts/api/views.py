from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from drf_spectacular.utils import extend_schema, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from accounts.models import CustomUser
from .serializers import UserDisplaySerializer, PasswordResetSerializer


##################
### User Views ###
##################

class CurrentUserAPIView(views.APIView):
    '''Get current logged user info'''
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        responses={
            200: UserDisplaySerializer,
            401: OpenApiResponse(description="Unauthorized", response=OpenApiTypes.OBJECT,),
        },
    )
    def get(self, request:Request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class UserPasswordResetAPIView(views.APIView):
    '''User Password Reset'''
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=PasswordResetSerializer,
        responses={
            200: OpenApiResponse(description="No response body", response=None),
            400: OpenApiResponse(response=OpenApiTypes.OBJECT,),
            401: OpenApiResponse(description="Unauthorized", response=OpenApiTypes.OBJECT,),
        },
    )
    def post(self, request:Request):
        # Get User:
        user = get_object_or_404(CustomUser, pk=request.user.id)
        # Validate Password:
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data['new_password']
        confirm_password = serializer.validated_data['confirm_password']
        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)
        # Update Password:
        user.set_password(new_password)
        user.password_must_be_reset = False
        user.save()
        return Response(status=200)
