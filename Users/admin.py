
# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'email')  # Customize the columns displayed in the user list

admin.site.register(User, CustomUserAdmin)  # Register your custom user model with the custom admin configuration

