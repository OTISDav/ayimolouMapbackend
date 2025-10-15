from django.urls import path
from .views import VendorListView, AddVendorView, NearbyVendorsView

urlpatterns = [
    path('', VendorListView.as_view(), name='vendor-list'),
    path('add/', AddVendorView.as_view(), name='vendor-add'),
    path('nearby/', NearbyVendorsView.as_view(), name='vendor-nearby'),
]
