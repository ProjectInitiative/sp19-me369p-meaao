"""
Renders HTML templates and handles backend logic for site
"""

import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Walkin, Contact


def index(request):
    """
    Renders the index page template
    """
    context = {}
    return render(request, 'index.html', context)


def signin(request):
    """
    Renders the signin page template and handles backend logic
    """
    auth_error = False
    if has_keys(['eid', 'password'], request.POST):
        user = authenticate(
            request, username=request.POST['eid'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(request.GET['redirect'] if 'redirect' in request.GET else '/')
        auth_error = True
    return render(request, 'signin.html', {
        'auth_error': auth_error
    })


def register(request):
    """
    Renders the register page template and handles backend logic
    """
    register_state = 'none'
    if (has_keys(['eid', 'email', 'password', 'first-name', 'last-name'], request.POST)
            and re.match(r'^[a-zA-Z]+\d*$', request.POST['eid'])):
        user = User.objects.create_user(
            username=request.POST['eid'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name']
        )
        if user is not None:
            register_state = 'success'
        else:
            register_state = 'error'
    return render(request, 'register.html', {
        'register_state': register_state
    })


def signout(request):
    """
    Renders the signout page template
    """
    logout(request)
    return render(request, 'signout.html', {})


def advisors(request):
    """
    Renders the advisors page template
    """
    return render(request, "advisors.html", {})


def contact(request):
    """
    Renders the contact page template
    """
    return render(request, "contact.html", {})


def forms(request):
    """
    Renders the forms page template
    """
    return render(request, "forms.html", {})


def resources(request):
    """
    Renders the resources page template
    """
    return render(request, "resources.html", {})


# Utility Functions

def has_keys(needles, haystack):
    """
    Searches for the existance of a set of needles in a haystack
    """
    return all(item in haystack for item in needles)
