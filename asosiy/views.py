from django.db.models import Sum, Avg
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from userapp.models import *

class HomeView(View):
    def get(self, request):
        data = {
            "user": MyUser.objects.get(username=request.user)
        }
        return render(request, 'header.html', data)

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/asosiy/')
        return render(request, 'page-index-2.html')

class HomeView2(View):
    def get(self, request):
        data = {
            "mahsulot": Mahsulot.objects.filter(chegirma__gt = 0).order_by('-chegirma')[:5],
            "bolimlar": Bolim.objects.all()[:7],
            "rasm": Media.objects.all(),
        }
        return render(request, 'page-index.html', data)

class BolimlarView(View):
    def get(self, request):
        data = {
            "bolimlar": Bolim.objects.all(),
            "mahsulot": Mahsulot.objects.all(),
        }
        return render(request, 'page-category.html', data)

class BittaBolimView(View):
    def get(self, request, id):
        data = {
            "bolim": Bolim.objects.get(id=id),
            "mahsulot": Mahsulot.objects.filter(bolim__id=id),
            "rasm": Media.objects.filter(mahsulot__bolim__id=id)
        }
        return render(request, 'page-listing-grid.html', data)

class BittaMahsulotView(View):
    def get(self, request, id):
        izohlar = Komment.objects.filter(mahsulot__id=id)
        orta = izohlar.aggregate(Avg('baho')).get('baho__avg')
        if orta:
            orta *= 20
        else:
            orta=0
        data = {
            "mahsulot": Mahsulot.objects.get(id=id),
            "rasm": Media.objects.filter(mahsulot__id=id),
            "koment": Komment.objects.filter(mahsulot__id=id),
            "koment_amount": Komment.objects.filter(mahsulot__id=id).count(),
            "yulduz": orta
        }
        return render(request, 'page-detail-product.html', data)
    def post(self, request, id):
        Komment.objects.create(
            username=MyUser.objects.get(username=request.user),
            text=request.POST.get('comment'),
            baho=request.POST.get('rating'),
            mahsulot=Mahsulot.objects.get(id=id),
        )
        return redirect(f'/asosiy/mahsulot/{id}/')

class ProfileView(View):
    def get(self, request, id):
        user = MyUser.objects.get(username=request.user)

        if request.user.id == id:
            data = {
                "user": user
            }
            return render(request, 'page-profile-main.html', data)
        return redirect('/asosiy/')
