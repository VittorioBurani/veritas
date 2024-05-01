from django.urls import path
from .views import (
    # GrapeVariety:
    GrapeVarietyListAPIView,
    GrapeVarietyRetrieveAPIView,
    GrapeVarietyCreateAPIView,
    GrapeVarietyUpdateAPIView,
    GrapeVarietyDestroyAPIView,
    # Producer:
    ProducerListAPIView,
    ProducerRetrieveAPIView,
    ProducerCreateAPIView,
    ProducerUpdateAPIView,
    ProducerDestroyAPIView,
    # Country:
    CountryListAPIView,
    CountryRetrieveAPIView,
    CountryCreateAPIView,
    CountryUpdateAPIView,
    CountryDestroyAPIView,
    # Region:
    RegionListAPIView,
    RegionRetrieveAPIView,
    RegionCreateAPIView,
    RegionUpdateAPIView,
    RegionDestroyAPIView,
    # Wine:
    WineListAPIView,
    WineRetrieveAPIView,
    WineCreateAPIView,
    WineUpdateAPIView,
    WineDestroyAPIView
)


urlpatterns = [
    # GrapeVariety:
    path('grape/create/',            GrapeVarietyCreateAPIView.as_view(),     name='grape-create'),
    path('grape/update/<int:pk>/',   GrapeVarietyUpdateAPIView.as_view(), name='grape-update'),
    path('grape/retrieve/<int:pk>/', GrapeVarietyRetrieveAPIView.as_view(),   name='grape-retrieve'),
    path('grape/list/',              GrapeVarietyListAPIView.as_view(),   name='grape-list'),
    path('grape/destroy/<int:pk>/',  GrapeVarietyDestroyAPIView.as_view(),  name='grape-destroy'),
    # Producer:
    path('producer/create/',            ProducerCreateAPIView.as_view(),     name='producer-create'),
    path('producer/update/<int:pk>/',   ProducerUpdateAPIView.as_view(), name='producer-update'),
    path('producer/retrieve/<int:pk>/', ProducerRetrieveAPIView.as_view(),   name='producer-retrieve'),
    path('producer/list/',              ProducerListAPIView.as_view(),   name='producer-list'),
    path('producer/destroy/<int:pk>/',  ProducerDestroyAPIView.as_view(),  name='producer-destroy'),
    # Country:
    path('country/create/',            CountryCreateAPIView.as_view(),     name='country-create'),
    path('country/update/<str:pk>/',   CountryUpdateAPIView.as_view(), name='country-update'),
    path('country/retrieve/<str:pk>/', CountryRetrieveAPIView.as_view(),   name='country-retrieve'),
    path('country/list/',              CountryListAPIView.as_view(),   name='country-list'),
    path('country/destroy/<str:pk>/',  CountryDestroyAPIView.as_view(),  name='country-destroy'),
    # Region:
    path('region/create/',            RegionCreateAPIView.as_view(),     name='region-create'),
    path('region/update/<int:pk>/',   RegionUpdateAPIView.as_view(), name='region-update'),
    path('region/retrieve/<int:pk>/', RegionRetrieveAPIView.as_view(),   name='region-retrieve'),
    path('region/list/',              RegionListAPIView.as_view(),   name='region-list'),
    path('region/destroy/<int:pk>/',  RegionDestroyAPIView.as_view(),  name='region-destroy'),
    # Wine:
    path('wine/create/',            WineCreateAPIView.as_view(),     name='wine-create'),
    path('wine/update/<int:pk>/',   WineUpdateAPIView.as_view(), name='wine-update'),
    path('wine/retrieve/<int:pk>/', WineRetrieveAPIView.as_view(),   name='wine-retrieve'),
    path('wine/list/',              WineListAPIView.as_view(),   name='wine-list'),
    path('wine/destroy/<int:pk>/',  WineDestroyAPIView.as_view(),  name='wine-destroy'),
]
