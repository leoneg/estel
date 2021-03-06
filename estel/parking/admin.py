from django.contrib import admin
from .models import Parking, Spot


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    model = Spot
    fields = ['active', 'status', 'parking', 'order_number']
    readonly_fields = ['parking', 'order_number', ]
    extra = 0

    def get_company_name(self, obj):
        return obj.parking.company.name
    get_company_name.admin_order_field = 'company'
    get_company_name.short_description = 'Company name'


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    model = Parking
    list_display = ('__str__', 'company', 'total_spots', 'available_spots', 'coordinates')
