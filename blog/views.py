from django.http import HttpResponse


def blog_index(request):
    return HttpResponse("Hello, world. You're on my blog index page.")