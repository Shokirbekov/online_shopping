from django.shortcuts import render
from django.views import View


class SavatView(View):
    def get(self, request):
        return render(request, 'page-shopping-cart.html')
class TanlanganView(View):
    def get(self, request):
        return render(request, 'page-profile-wishlist.html')
class BuyurtmaView(View):
    def get(self, request):
        return render(request, 'page-profile-orders.html')