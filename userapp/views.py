from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')
    def post(self, request):
        a = authenticate(
            username=request.POST.get('u'),
            password=request.POST.get('p')
        )

        if a:
            login(request, a)
            return redirect('/asosiy/')
        return redirect('/user/login/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class RegisterView(View):
    def post(self, request):
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )

        MyUser.objects.create(
            username=request.POST.get('l'),
            f_name = request.POST.get('f_name'),
            l_name = request.POST.get('l_name'),
            email = request.POST.get('email'),
            gender=request.POST.get('gender'),
            city=request.POST.get('city'),
            country=request.POST.get('cny'),
        )
        return redirect('/user/login/')
    def get(self, request):
        return render(request, 'page-user-register.html')