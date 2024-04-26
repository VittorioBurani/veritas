from django.urls import path, include


urlpatterns = [
    path('api/', include("wine_cellar.api.urls")),
]
