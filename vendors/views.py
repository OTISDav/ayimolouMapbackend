from rest_framework import generics, permissions
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from math import radians, sin, cos, sqrt, atan2


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calcule la distance entre deux points GPS (en km)."""
    R = 6371.0
    lat1_r, lon1_r, lat2_r, lon2_r = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2_r - lon1_r
    dlat = lat2_r - lat1_r
    a = sin(dlat / 2)**2 + cos(lat1_r) * cos(lat2_r) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


class VendorListView(generics.ListAPIView):
    """Liste de tous les vendeurs (visibles sur la carte)."""
    queryset = Vendor.objects.filter(verified=True, available=True)
    serializer_class = VendorSerializer
    permission_classes = [permissions.AllowAny]


class AddVendorView(generics.CreateAPIView):
    """Ajout d’un vendeur (doit être connecté)."""
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NearbyVendorsView(APIView):
    """Retourne les vendeurs proches d’une position GPS."""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            lat = float(request.query_params.get("lat"))
            lon = float(request.query_params.get("lon"))
            radius = float(request.query_params.get("radius", 3))  # km par défaut
        except (TypeError, ValueError):
            return Response({"error": "Paramètres lat/lon invalides"}, status=400)

        vendors = Vendor.objects.filter(verified=True, available=True)
        nearby = []
        for vendor in vendors:
            distance = calculate_distance(lat, lon, vendor.latitude, vendor.longitude)
            if distance <= radius:
                vendor.distance = round(distance, 2)
                nearby.append(vendor)

        serializer = VendorSerializer(nearby, many=True)
        return Response(serializer.data)
