"""
Registering models with the admin handler
"""

from django.contrib import admin

from .models import Walkin, Contact


admin.site.register(Walkin)
admin.site.register(Contact)
