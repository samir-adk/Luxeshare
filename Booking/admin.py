# admin.py

from django.contrib import admin
from .models import BookingCar

@admin.register(BookingCar)
class BookingCarAdmin(admin.ModelAdmin):
    list_display = ['user', 'vehicle', 'start_time', 'end_time', 'total_cost', 'booked', 'cancelled', 'hourly_rate']
    search_fields = ['user__username', 'vehicle__registration_number']  # Add fields to search
    list_filter = ['booked', 'cancelled']  # Add fields to filter
    date_hierarchy = 'start_time'  # Add date hierarchy
    readonly_fields = ['total_cost']  # Make total_cost readonly
    fieldsets = [
        (None, {'fields': ['user', 'vehicle', 'start_time', 'end_time', 'booked', 'cancelled', 'hourly_rate']}),
        ('Additional Information', {'fields': ['total_cost'], 'classes': ['collapse']}),
    ]  # Customize fieldsets for better organization



    def order_by_latest(self, request, queryset):
        self.model._meta.ordering = ['-created_at']
        return queryset

    def order_by_oldest(self, request, queryset):
        self.model._meta.ordering = ['created_at']
        return queryset
        
    def get_actions(self, request):
        actions = super().get_actions(request)
        actions['order_by_latest'] = (self.order_by_latest, 'order_by_latest', 'Order by Latest Created')
        actions['order_by_oldest'] = (self.order_by_oldest, 'order_by_oldest', 'Order by Oldest Created')
        return actions
