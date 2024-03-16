from django.contrib import admin
from Car.models import CarCategory,CarCompany,Vehicle
# Register your models here.

admin.site.register(CarCategory)
admin.site.register(CarCompany)
admin.site.register(Vehicle)
