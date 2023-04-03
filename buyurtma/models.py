from django.db import models
from django.contrib.auth.models import User
from userapp.models import *
from asosiy.models import *


class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    soni = models.SmallIntegerField()
    umumiy = models.SmallIntegerField(blank=True, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"mana {self.umumiy}"

class Wishes(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)

class Manzil(models.Model):
    tel = models.SmallIntegerField()
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    manzil = models.TextField()
    zipcode = models.SmallIntegerField()
    shahar = models.TextField()
    davlat = models.TextField()
    asosiy = models.BooleanField(default=False)
    def __str__(self):
        return self.manzil

class Buyurtma(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    sana = models.DateTimeField(auto_now_add=True)
    manzil = models.ForeignKey(Manzil, on_delete=models.CASCADE)
    savat = models.ManyToManyField(Savat)
    holat = models.TextField()
    summa = models.IntegerField()
    yetkaish_narxi = models.IntegerField()
    def __str__(self):
        return self.holat