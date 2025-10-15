from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField(read_only=True)  # pour affichage optionnel

    class Meta:
        model = Vendor
        fields = [
            'id', 'user', 'name', 'phone', 'latitude', 'longitude',
            'description', 'price', 'available', 'verified', 'created_at', 'distance'
        ]
        read_only_fields = ['user', 'verified', 'created_at']

    def get_distance(self, obj):
        # affichage optionnel : ajouté dans la vue si la distance est calculée
        return getattr(obj, "distance", None)
