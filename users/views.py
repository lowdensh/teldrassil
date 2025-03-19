from django.shortcuts import render


def users_home(request):
  context = {}
  return render(request, 'users/home.html', context)

def users_stylish(request):
  context = {}
  return render(request, 'users/stylish.html', context)
