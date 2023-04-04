from django.contrib import admin
from .models import Flat, Complain, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ['address', 'price',
                    'new_building',
                    'construction_year',
                    'town',
                    'owners_phonenumber',
                    'owner_pure_phone',
                    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner', 'phonenumber', 'pure_phone']
    raw_id_fields = ['flats']
