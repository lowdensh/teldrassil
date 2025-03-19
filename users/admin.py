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
    'email',
    'first_name',
    'last_name',
    'is_superuser',
    'is_staff',
    'last_login',
  )
  ordering = (
    'email',
    'first_name',
    'last_name',
    'is_superuser',
    'is_staff',
  )
  search_fields = (
    'email',
    'first_name',
    'last_name',
  )
  list_filter = (
    'is_superuser',
    'is_staff',
  )
  list_display_links = ('email', )

  # Specific CustomUser instance
  prepopulated_fields = {'slug': ('first_name', 'last_name')}
  fieldsets = (
    ('Account', {'fields': (
      'email',
      'first_name',
      'last_name',
      'password',
      'slug',
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
      'slug',
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