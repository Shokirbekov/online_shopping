from django.db import models
from django.contrib.auth.models import User
from userapp.models import *

class Bolim(models.Model):
    nom = models.CharField(max_length=500)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=500)
    narx = models.PositiveIntegerField()
    brend = models.CharField(max_length=500)
    davlat = models.CharField(max_length=500)
    kafolat = models.CharField(max_length=500)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    min_miqdor = models.PositiveSmallIntegerField(default=1)
    tasdiqlangan = models.BooleanField(default=True)
    yetkazish = models.CharField(max_length=500, default='3-4 kun')
    mavjud = models.BooleanField(default=True)
    chegirma = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    def __str__(self):
        return self.mahsulot.nom

class Komment(models.Model):
    username = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=1000)
    baho = models.PositiveSmallIntegerField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, blank=True, null=True)
    sana = models.DateTimeField(auto_now_add=True, blank=True, null=True)