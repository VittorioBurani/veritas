from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from wine_cellar.models import GrapeVariety, Producer, Country, Region, Wine
from .serializers import (
    GrapeVarietySerializer,
    ProducerSerializer,
    CountrySerializer,
    RegionSerializer,
    CountryDisplaySerializer,
    RegionDisplaySerializer,
    WineSerializer,
    WineDisplaySerializer,
)
from .filters import (
    GrapeVarietyFilter,
    ProducerFilter,
    CountryFilter,
    RegionFilter,
    WineFilter,
)


##########################
### GrapeVariety Views ###
##########################

class GrapeVarietyListAPIView(generics.ListAPIView):
    '''Obtain all grape varieties'''
    queryset = GrapeVariety.objects.all()
    serializer_class = GrapeVarietySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GrapeVarietyFilter


class GrapeVarietyRetrieveAPIView(generics.RetrieveAPIView):
    '''Obtain a specific grape variety'''
    queryset = GrapeVariety.objects.all()
    serializer_class = GrapeVarietySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)


class GrapeVarietyCreateAPIView(generics.CreateAPIView):
    '''Create a new grape variety'''
    serializer_class = GrapeVarietySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class GrapeVarietyUpdateAPIView(generics.UpdateAPIView):
    '''Update a specific grape variety'''
    queryset = GrapeVariety.objects.all()
    serializer_class = GrapeVarietySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class GrapeVarietyDestroyAPIView(generics.DestroyAPIView):
    '''Delete a specific grape variety'''
    queryset = GrapeVariety.objects.all()
    serializer_class = GrapeVarietySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


##########################
### Producer Views ###
##########################

class ProducerListAPIView(generics.ListAPIView):
    '''Obtain all producers'''
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProducerFilter


class ProducerRetrieveAPIView(generics.RetrieveAPIView):
    '''Obtain a specific producer'''
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProducerCreateAPIView(generics.CreateAPIView):
    '''Create a new producer'''
    serializer_class = ProducerSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class ProducerUpdateAPIView(generics.UpdateAPIView):
    '''Update a specific producer'''
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class ProducerDestroyAPIView(generics.DestroyAPIView):
    '''Delete a specific producer'''
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


##########################
### Country Views ###
##########################

class CountryListAPIView(generics.ListAPIView):
    '''Obtain all wine production countries'''
    queryset = Country.objects.all()
    serializer_class = CountryDisplaySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CountryFilter


class CountryRetrieveAPIView(generics.RetrieveAPIView):
    '''Obtain a specific wine production country'''
    queryset = Country.objects.all()
    serializer_class = CountryDisplaySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)


class CountryCreateAPIView(generics.CreateAPIView):
    '''Create a new wine production country'''
    serializer_class = CountrySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class CountryUpdateAPIView(generics.UpdateAPIView):
    '''Update a specific wine production country'''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class CountryDestroyAPIView(generics.DestroyAPIView):
    '''Delete a specific wine production country'''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


##########################
### Region Views ###
##########################

class RegionListAPIView(generics.ListAPIView):
    '''Obtain all wine production regions'''
    queryset = Region.objects.all()
    serializer_class = RegionDisplaySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RegionFilter


class RegionRetrieveAPIView(generics.RetrieveAPIView):
    '''Obtain a specific wine production region'''
    queryset = Region.objects.all()
    serializer_class = RegionDisplaySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)


class RegionCreateAPIView(generics.CreateAPIView):
    '''Create a new wine production region'''
    serializer_class = RegionSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class RegionUpdateAPIView(generics.UpdateAPIView):
    '''Update a specific wine production region'''
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class RegionDestroyAPIView(generics.DestroyAPIView):
    '''Delete a specific wine production region'''
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


##########################
### Wine Views ###
##########################

class WineListAPIView(generics.ListAPIView):
    '''Obtain all wines'''
    queryset = Wine.objects.all()
    serializer_class = WineDisplaySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WineFilter


class WineRetrieveAPIView(generics.RetrieveAPIView):
    '''Obtain a specific wine'''
    queryset = Wine.objects.all()
    serializer_class = WineDisplaySerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)


class WineCreateAPIView(generics.CreateAPIView):
    '''Create a new wine'''
    serializer_class = WineSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class WineUpdateAPIView(generics.UpdateAPIView):
    '''Update a specific wine'''
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)


class WineDestroyAPIView(generics.DestroyAPIView):
    '''Delete a specific wine'''
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    authentication_classes = (JWTStatelessUserAuthentication,)
    permission_classes = (IsAdminUser,)
