from django.http import HttpResponse


def home(request):
    return HttpResponse("Home Page..")

def blog(request):
    return HttpResponse("Blog lives here")