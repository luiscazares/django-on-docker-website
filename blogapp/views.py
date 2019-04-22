from django.http import HttpResponse


def index(request):
    return HttpResponse("My blog will one day live...")