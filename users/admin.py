# https://testdriven.io/blog/django-custom-user-model/

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Main list
    list_display = (
        'is_superuser',
        'is_staff',
        'email',
        'last_name',
        'first_name',
        'last_login',
    )
    ordering = (
        'is_superuser',
        'is_staff',
        'email',
        'last_name',
        'first_name',
    )
    search_fields = (
        'email',
        'last_name',
        'first_name',
    )
    list_filter = (
        'is_superuser',
        'is_staff',
    )
    list_display_links = ('email', )

    # Specific CustomUser instance
    fieldsets = (
        ('Account', {'fields': (
             'email',
             'first_name',
             'last_name',
             'password',
        )}),
        ('Dates', {'fields': (
            'date_joined',
            'last_login',
        )}),
        ('Permissions', {'fields': (
            'is_superuser',
            'is_staff',
            'is_active',
        )}),
    )
    add_fieldsets = (
        ('Account', {'fields': (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )}),
        ('Permissions', {'fields': (
            'is_superuser',
            'is_staff',
        )}),
    )
    readonly_fields = [
        'date_joined',
        'last_login',
    ]