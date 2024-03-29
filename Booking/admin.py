from django.contrib import admin
from .models import BookingCar
from datetime import timedelta

class BookingCarAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'start_time', 'end_time', 'duration_hours', 'total_cost', 'booked')
    readonly_fields = ('duration_hours',)

    def duration_hours(self, obj):
        # Calculate duration in hours
        duration = obj.end_time - obj.start_time
        return duration.total_seconds() / 3600

    duration_hours.short_description = 'Duration (hours)'

admin.site.register(BookingCar, BookingCarAdmin)
