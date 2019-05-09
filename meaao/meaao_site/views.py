"""
Renders HTML templates and handles backend logic for site
"""

import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.http import JsonResponse
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
        # Creates a new contact
        message = Contact(
            recipient=request.POST['recipient'],
            user_name=request.POST['name'],
            user_eid=request.POST['eid'],
            user_email=request.POST['email'],
            message=request.POST['message'])
        message.save()

    # Delete message
    if 'delete_id' in request.POST and request.user.has_perm('meaao_site.delete_contact'):
        Contact.objects.filter(id=request.POST['delete_id']).delete()

    # Retrieve message
    messages = []
    if request.user.has_perm('meaao_site.view_contact'):
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


def walkins(request):
    """
    Renders the walkins page template and handles the backend logic
    """

    # Get advisors
    advisor_users = User.objects.filter(groups__name__in=['advisors']).all()

    # Perform actions
    if 'action' in request.POST:
        walkin = Walkin.objects.filter(id=request.POST['id'])
        if not walkin.exists():
            walkin = None
        else:
            walkin = walkin.first()
        if request.user.has_perm('meaao_site.view_walkin') or walkin.user_id == request.user.id:
            if request.POST['action'] == 'walkin_save':
                walkin.advisor_id = request.POST['advisor_id']
                walkin.comments = request.POST['comments']
                walkin.save()
            elif request.POST['action'] == 'walkin_take':
                Walkin.objects.filter(order__gt=max(
                    0, walkin.order)).update(order=F('order') - 1)
                walkin.order = -1
                walkin.save()
            elif request.POST['action'] == 'walkin_up' or request.POST['action'] == 'walkin_down':
                move_direction = - \
                    1 if request.POST['action'] == 'walkin_up' else 1
                Walkin.objects.filter(
                    order=walkin.order + move_direction).update(order=F('order') - move_direction)
                walkin.order = F('order') + move_direction
                walkin.save()
            elif request.POST['action'] == 'walkin_delete':
                Walkin.objects.filter(order__gt=max(
                    0, walkin.order)).update(order=F('order') - 1)
                walkin.delete()

    # Get current user's walkins
    if request.user.has_perm('meaao_site.view_walkin'):
        walkins_results = Walkin.objects.select_related(
            'user').all().order_by('order', 'id')
    else:
        walkins_results = Walkin.objects.select_related('user').filter(
            user=request.user).all().order_by('order', 'id')
    user_walkins = []
    for walkin in walkins_results:
        user_walkins.append({
            'id': walkin.id,
            'user_name': walkin.user.get_full_name(),
            'advisor_id': walkin.advisor_id,
            'comments': walkin.comments,
            'order': walkin.order
        })

    # Update API
    if 'result' in request.GET:
        return JsonResponse({
            'walkins': user_walkins,
            'user': {
                'grants': list(request.user.get_all_permissions())
            }
        })
    if 'search_student' in request.GET:
        query = request.GET['q']
        users = list(User.objects.filter(Q(username__icontains=query) | Q(
            first_name__icontains=query) | Q(last_name__icontains=query))[:20].only().values())
        return JsonResponse({
            'results': list(map(lambda user: {
                'id': user['id'],
                'text': user['username'],
                'data': [user['username'], '{} {}'.format(user['first_name'], user['last_name'])]
            }, users))
        })

    # Add new walkin
    if ('advisor' in request.POST and
            (user_walkins or request.user.has_perm('meaao_site.view_walkin'))):
        new_walkin = Walkin(
            user=User.objects.get(id=request.POST['student'] if request.user.has_perm(
                'meaao_site.view_walkin') else request.user.id),
            advisor=User.objects.get(id=request.POST['advisor']),
            comments=request.POST['comments'],
            order=(Walkin.objects.latest(
                'order').order if Walkin.objects.exists() else -1) + 1
        )
        new_walkin.save()

    return render(request, "walkins.html", {
        'advisors': advisor_users
    })


# Utility Functions

def has_keys(needles, haystack):
    """
    Searches for the existence of a set of needles in a haystack
    """
    return all(item in haystack for item in needles)
