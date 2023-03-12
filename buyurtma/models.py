from django.db import models
from django.contrib.auth.models import User
from userapp.models import *
from asosiy.models import *


class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    soni = models.SmallIntegerField()
    wished = models.BooleanField(default=False)
    umumiy = models.SmallIntegerField(blank=True, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)

class Wishes(models.Model):
    mahsulot = models.ForeignKey(Savat, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)