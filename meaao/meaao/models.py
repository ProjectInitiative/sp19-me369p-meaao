from django.db import models
from django.conf import settings


class Walkins(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    advisor_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    order = models.IntegerField()
    comments = models.TextField()


class Contact(models.Model):
    recipient = models.CharField()
    user_name = models.CharField()
    user_eid = models.CharField(max_length=255)
    user_email = models.CharField()
    message = models.TextField()
