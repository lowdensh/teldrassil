from . import views
from django.urls import path


appname = 'users'
urlpatterns = [
    path('', views.home, name='users-home'),
    path('stylish/', views.stylish, name='users-stylish'),
]
