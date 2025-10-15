from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'phone', 'latitude', 'longitude', 'available', 'verified', 'created_at')
    list_filter = ('available', 'verified')
    search_fields = ('name', 'phone', 'user__username')
    ordering = ('id',)
