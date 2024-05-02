from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email_link', 'phone_number', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

    def email_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.pk] )
        return format_html('<a href="{}">{}</a>', url, obj.email)
    email_link.short_description = 'Email'

admin.site.register(CustomUser, CustomUserAdmin)
