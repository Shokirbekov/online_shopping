from django.db import models
from userapp.models import *
from asosiy.models import *

class Wishes(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)