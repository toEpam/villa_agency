from django.urls import path
from .views import HomePageView, ContactPageView, PropertiesPageView, PropertyDetailsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('properties', PropertiesPageView.as_view(), name='properties'),
    path('property_details', PropertyDetailsPageView.as_view(), name='property_details'),
]
