"""
Django database models
"""

from django.db import models
from django.contrib.auth.models import User


class Walkin(models.Model):
    """
    Model to store data on each walkin (for the "Walk-Ins" page)
    """
    user = models.ForeignKey(
        User, related_name='+', on_delete=models.PROTECT, null=True)
    advisor = models.ForeignKey(
        User, related_name='+', on_delete=models.PROTECT, null=True)
    order = models.IntegerField()
    comments = models.TextField()


class Contact(models.Model):
    """
    Model to store data on each message (for the "Contact Us" page)
    """
    recipient = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_eid = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    message = models.TextField()
