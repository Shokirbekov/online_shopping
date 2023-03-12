from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import *
from asosiy.models import *


class SavatView(View):
    def get(self, request):
        a = "Savatda hech nima yo'q. Biror nima buyurib, qayting!"
        savatlar = Savat.objects.filter(user__username=request.user)
        summa = savatlar.aggregate(Sum('umumiy')).get('umumiy__sum')
        chegirmalar = 0
        if savatlar:
            for savat in savatlar:
                chegirmalar += savat.soni * (savat.mahsulot.chegirma * savat.mahsulot.narx) / 100
        else:
            return render(request, 'page-cart-error.html')
        data = {
            "savat": Savat.objects.filter(user=MyUser.objects.get(username=request.user)),
            'summa': summa,
            'chg': round(chegirmalar, 2),
            'yakuniy': summa - round(chegirmalar, 2),
            "error": a,
            "wish": Wishes.objects.filter(user=MyUser.objects.get(username=request.user))
        }
        return render(request, 'page-shopping-cart.html', data)
class TanlanganView(View):
    def get(self, request):
        return render(request, 'page-profile-wishlist.html')
class BuyurtmaView(View):
    def get(self, request):
        return render(request, 'page-profile-orders.html')

class QoshView(View):
    def get(self, request, id):
        savat = Savat.objects.get(id=id)
        if savat.user.username == request.user:
            narx = savat.mahsulot.narx
            savat.umumiy += narx
            savat.soni += 1
            savat.save()
        return redirect('/buyurtma/savat/')

class AyirView(View):
    def get(self, request, id):
        savat = Savat.objects.get(id=id)
        narx = savat.mahsulot.narx
        if savat.soni !=1 and savat.user.username==request.user:
            savat.soni -= 1
            savat.umumiy -= narx
        savat.save()
        return redirect('/buyurtma/savat/')

class OchirView(View):
    def get(self, request, id):
        to_be_deleted = Savat.objects.get(id=id)
        if to_be_deleted.user.username == request.user:
            to_be_deleted.delete()
            return redirect('/buyurtma/savat/')

class QoshishView(View):
    def get(self, request, id):
        savat = Mahsulot.objects.get(id=id)
        Savat.objects.create(
            mahsulot = savat,
            soni=1,
            umumiy=savat.narx,
            user=MyUser.objects.get(username=request.user)
        )
        return redirect('/buyurtma/savat/')

class TanlanganQoshishView(View):
    def get(self, request, id):
        savat = Savat.objects.get(id=id)
        Wishes.objects.create(
            mahsulot=savat,
            user=MyUser.objects.get(username=request.user)
        )
        savat.wished = True
        savat.save()
        return redirect('/buyurtma/savat/')

class TanlanganDeleteView(View):
    def get(self, request, id):
        savat = Savat.objects.get(id=id)
        to_be_deleted = Wishes.objects.get(mahsulot__id=id)
        if to_be_deleted.user.username == request.user:
            savat.wished = False
            to_be_deleted.delete()
            savat.save()
            return redirect('/buyurtma/savat/')
        else:
            return render(request, 'id-error.html')

class WishlistView(View):
    def get(self, request):
        data = {
            "wishes": Wishes.objects.filter(user__username=request.user)
        }
        return render(request, 'page-profile-wishlist.html', data)

class WishDeleteView(View):
    def get(self, request, id):
        savat = Savat.objects.get(id=id)
        to_be_deleted = Wishes.objects.get(mahsulot__id=id)
        if to_be_deleted.user.username == request.user:
            savat.wished = False
            to_be_deleted.delete()
            savat.save()
            return redirect('/buyurtma/wishlist/')
        else:
            return render(request, 'id-error.html')