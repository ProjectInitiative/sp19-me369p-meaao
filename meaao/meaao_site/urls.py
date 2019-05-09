from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('advisors/', views.advisors, name='advisors'),
    path('contact/', views.contact, name='contact'),
    path('walkins/', views.walkins, name='walkins'),
    path('forms/', views.forms, name='forms'),
    path('resources/', views.resources, name='resources'),
]
