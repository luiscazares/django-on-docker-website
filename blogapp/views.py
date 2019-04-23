from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404


def index(request):
    context = {}
    template = 'blogapp/home.html'
    return render(request, template, context)


def blog(request):
    context = {}
    template = 'blogapp/blog.html'
    return render(request, template, context)