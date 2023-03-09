from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    f_name = models.CharField(max_length=500, blank=True)
    l_name = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.l_name