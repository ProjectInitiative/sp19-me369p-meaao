from django.http import HttpResponse
from django.shortcuts import render

from .models import Walkin, Contact


def index(request):
    context = {}
    return render(request, 'index.html', context)
