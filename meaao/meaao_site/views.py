from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.defaulttags import csrf_token

from .models import Walkin, Contact


def index(request):
    context = {}
    return render(request, 'index.html', context)

def signin(request):
    auth_error = False
    if 'eid' in request.POST and 'password' in request.POST:
        user = authenticate(request, username=request.POST['eid'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(request.GET['redirect'] if 'redirect' in request.GET else '/')
        else:
            auth_error = True
    return render(request, 'signin.html', {
        'auth_error': auth_error
    })

def signout(request):
    logout(request)
    return render(request, 'signout.html', {})

def advisors(request):
    return render(request, "advisors.html", {})

def contact(request):
    return render(request, "contact.html", {})

def forms(request):
    return render(request, "forms.html", {})

def resources(request):
    return render(request, "resources.html", {})


