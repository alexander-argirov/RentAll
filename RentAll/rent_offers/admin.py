from django.contrib import admin

from RentAll.rent_offers.models import Car, Van, CampersCaravans


@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'car_type', 'type_of_engine', 'first_registration',
                    'seats', 'vehicle_image', 'price', 'city', 'published', 'owner',)
    ordering = ('published', 'brand', 'model', 'first_registration')
    list_filter = ('brand', 'model', 'type_of_engine', 'first_registration', 'price', 'owner')
    search_fields = ('brand', 'model', 'type_of_engine', 'first_registration', 'price',)


@admin.register(Van)
class VansAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'type_of_engine', 'first_registration',
                    'seats', 'payload_weight', 'vehicle_image', 'price', 'city', 'published', 'owner',)
    ordering = ('published', 'brand', 'model', 'first_registration')
    list_filter = ('brand', 'model', 'type_of_engine', 'price', 'owner')
    search_fields = ('brand', 'model', 'first_registration', 'price',)


@admin.register(CampersCaravans)
class CampersCaravansAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'type_of_engine', 'first_registration',
                    'seats', 'type', 'vehicle_image', 'price', 'city', 'published', 'owner',)
    ordering = ('published', 'brand', 'model', 'first_registration')
    list_filter = ('brand', 'model', 'type_of_engine', 'price', 'owner')
    search_fields = ('brand', 'model', 'first_registration', 'price',)
