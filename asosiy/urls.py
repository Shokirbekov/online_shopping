from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView2.as_view()),
    path('bolimlar/', BolimlarView.as_view()),
    path('bolim/<int:id>/', BittaBolimView.as_view()),
    path('mahsulot/<int:id>/', BittaMahsulotView.as_view()),
]