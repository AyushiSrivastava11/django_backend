from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World, this in Home page.")


def about(request):
    return HttpResponse("Hello World, this in About page.")


def contact(request):
    return HttpResponse("Hello World, this in Contact page.")
