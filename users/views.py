from django.shortcuts import render


def home(request):
  context = {}
  return render(request, 'users/home.html', context)
