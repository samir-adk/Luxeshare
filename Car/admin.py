from django.contrib import admin
from Car.models import CarCategory,CarCompany,Vehicle,Owner
# Register your models here.



# admin.py

from django.contrib import admin
from .models import CarCategory, CarCompany, Owner, Vehicle, VehicleImage

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ['car_category_name', 'Note']
    search_fields = ['car_category_name']
    date_hierarchy = 'created_at'
    list_filter = ['car_category_name']



@admin.register(CarCompany)
class CarCompanyAdmin(admin.ModelAdmin):
    list_display = ['car_company_category', 'car_company_name','created_at','updated_at']
    search_fields=['car_company_category', 'car_company_name']
    date_hierarchy = 'created_at'

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address','created_at','updated_at']
    search_fields=['name', 'email', 'phone_number', 'address']
    date_hierarchy = 'created_at'

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['owner', 'model', 'year', 'color', 'registration_number', 'hourly_rate','created_at','updated_at']
    search_fields=['owner__name','model','registration_number']
    date_hierarchy = 'created_at'

@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'image']
   
