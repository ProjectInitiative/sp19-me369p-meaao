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
    return render(request, 'index.html', {})


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


def account(request):
    """
    Renders the register page template and handles backend logic
    """
    account_state = 'none'
    if request.user.is_authenticated and 'action' in request.POST:
        account_state = 'error'
        if (request.POST['action'] == 'change-password'
                and has_keys(['current-password', 'new-password1', 'new-password2'], request.POST)
                and request.POST['new-password1'] == request.POST['new-password2']
                and request.POST['new-password1'] != request.POST['current-password']
                and request.user.check_password(request.POST['current-password'])):
            request.user.set_password(request.POST['new-password1'])
            request.user.save()
            account_state = 'success_password'
        if request.POST['action'] == 'change-email' and 'email' in request.POST:
            request.user.email = request.POST['email']
            request.user.save()
            account_state = 'success_email'
        elif (request.POST['action'] == 'change-name'
                and has_keys(['first-name', 'last-name'], request.POST)):
            request.user.first_name = request.POST['first-name']
            request.user.last_name = request.POST['last-name']
            request.user.save()
            account_state = 'success_name'
    return render(request, 'account.html', {
        'account_state': account_state
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
    Renders the contact page template and handles backend logic
    """

    if has_keys(['recipient', 'name', 'eid', 'email', 'message'], request.POST):
        # Adds new contact to database
        contact = Contact(
            recipient=request.POST['recipient'],
            user_name=request.POST['name'],
            user_eid=request.POST['eid'],
            user_email=request.POST['email'],
            message=request.POST['message']
        )
        contact.save()

    # Delete message
    if 'delete_id' in request.POST and request.user.has_perms('contact_accessother'):
        Contact.objects.filter(id=id).delete()

    # Retrieve messages
    messages = []
    if request.user.has_perms('contact_accessother'):
        messages = Contact.objects

    return render(request, "contact.html", {
        'messages': messages
    })


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
    Searches for the existence of a set of needles in a haystack
    """
    return all(item in haystack for item in needles)
