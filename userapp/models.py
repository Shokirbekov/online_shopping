from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=500, blank=True)
    f_name = models.CharField(max_length=500, blank=True)
    l_name = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.l_name