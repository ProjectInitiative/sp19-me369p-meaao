from django.http import HttpResponse
from django.shortcuts import render

from .models import Walkin, Contact


def index(request):
    context = {}
    return render(request, 'index.html', context)

def advisors(request):
    return render(request, "advisors.html", {})

def contact(request):
    return render(request, "contact.html", {})

def forms(request):
    return render(request, "forms.html", {})

def resources(request):
    return render(request, "resources.html", {})


