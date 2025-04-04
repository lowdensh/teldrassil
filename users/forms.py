# https://testdriven.io/blog/django-custom-user-model/

from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(
    max_length=30,
    help_text='Your forename. Does not need to be unique.'
  )
  last_name = forms.CharField(
    max_length=30,
    help_text='Your surname. Does not need to be unique.'
  )
  slug = forms.SlugField(
    max_length=30,
    help_text='Will be shown in the web URL to refer to you.'
  )

  class Meta(UserCreationForm):
    model = CustomUser
    fields = (
      'email',
      'first_name',
      'last_name',
      'slug',
      'password1',
      'password2',
    )


class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = (
      'email',
      'first_name',
      'last_name',
      'slug',
      'password',
    )