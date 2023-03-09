from django.urls import path
from .views import *

urlpatterns = [
    path('savat/', SavatView.as_view()),
    path('wishlist/', TanlanganView.as_view()),
    path('orders/', BuyurtmaView.as_view()),
]