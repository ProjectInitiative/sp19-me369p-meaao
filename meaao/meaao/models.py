from django.db import models


class Users(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    
class Sessions(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE)
    created = models.DateField()
    last_seen = models.DateField()
    

