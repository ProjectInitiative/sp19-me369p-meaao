from django.db import models
from django.conf import settings


class Walkin(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='advisee', on_delete=models.PROTECT)
    advisor_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='advisor', on_delete=models.PROTECT)
    order = models.IntegerField()
    comments = models.TextField()


class Contact(models.Model):
    recipient = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_eid = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    message = models.TextField()
