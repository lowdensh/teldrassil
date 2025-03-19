from . import views
from django.urls import path


appname = 'users'
urlpatterns = [
    path(
      '',
      views.users_home,
      name='users_home'),
    path(
      'stylish/',
      views.users_stylish,
      name='users_stylish'),
]
