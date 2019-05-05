from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('advisors/', views.advisors, name='advisors'),
    path('contact/', views.contact, name='contact'),
    path('forms/', views.forms, name='forms'),
    path('resources/', views.resources, name='resources'),
]
