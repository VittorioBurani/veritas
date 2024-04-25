from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from drf_spectacular.utils import extend_schema
from .serializers import UserDisplaySerializer


##################
### User Views ###
##################

class CurrentUserAPIView(views.APIView):
    '''Get current logged user info'''
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        responses={200: UserDisplaySerializer},
    )
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)
