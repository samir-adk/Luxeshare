from django.contrib import admin
from AboutUs.models import ContactUs
# Register your models here.
@admin.register(ContactUs)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['email','message','created_at','updated_at']
    search_fields=['email']
    date_hierarchy = 'created_at'