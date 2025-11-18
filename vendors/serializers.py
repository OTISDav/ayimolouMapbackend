from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField(read_only=True)  # pour affichage optionnel
    photo = serializers.SerializerMethodField()  # <--- on remplace le champ pour corriger l'URL

    class Meta:
        model = Vendor
        fields = [
            'id', 'user', 'name', 'photo', 'phone', 'latitude', 'longitude',
            'description', 'price', 'available', 'verified', 'created_at', 'distance'
        ]
        read_only_fields = ['user', 'verified', 'created_at']

    def get_distance(self, obj):
        # affichage optionnel : ajouté dans la vue si la distance est calculée
        return getattr(obj, "distance", None)

    def get_photo(self, obj):
        if obj.photo:
            # si tu gardes resource_type="raw", on retire "raw/upload/" pour avoir l'URL complète
            return str(obj.photo).replace("raw/upload/", "")
        return None
