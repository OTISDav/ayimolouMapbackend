from django.urls import path
from . views import VendorListView, AddVendorView, NearbyVendorsView
from . import views  # Ajoutez cet import


urlpatterns = [
    path('', VendorListView.as_view(), name='vendor-list'),
    path('add/', AddVendorView.as_view(), name='vendor-add'),
    path('nearby/', NearbyVendorsView.as_view(), name='vendor-nearby'),

    path('add-page/', views.add_vendor_page, name='add-vendor-page'),
]
