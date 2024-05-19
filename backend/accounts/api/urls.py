from django.urls import path
from .views import (
    CurrentUserAPIView,
    UserPasswordResetAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # Generic user views:
    path('get-user/', CurrentUserAPIView.as_view(), name='get-user'),
    path('password-reset/', UserPasswordResetAPIView.as_view(), name='password-reset'),
    # Simple JWT:
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
