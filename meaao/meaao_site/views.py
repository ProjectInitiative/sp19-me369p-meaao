from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html", {})

def advisors(request):
    return render(request, "advisors.html", {})

def contact(request):
    return render(request, "contact.html", {})

def forms(request):
    return render(request, "forms.html", {})

def resources(request):
    return render(request, "resources.html", {})


