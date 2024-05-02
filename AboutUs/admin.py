from django.contrib import admin
from AboutUs.models import ContactUs
# Register your models here.
@admin.register(ContactUs)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['email','phone','message','created_at','updated_at']
    search_fields=['email','phone']
    date_hierarchy = 'created_at'