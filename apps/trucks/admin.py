from django.contrib import admin

from apps.trucks.models import Truck, TruckModel, Trip


@admin.register(TruckModel)
class TruckModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    pass


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    fields = ['truck', 'current_weight', 'date_started', 'date_ended']
    readonly_fields = ['date_started']
