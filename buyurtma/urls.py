from django.urls import path
from .views import *

urlpatterns = [
    path('savat/', SavatView.as_view()),
    path('orders/', BuyurtmaView.as_view()),
    path('savat_q/<int:id>/', QoshView.as_view()),
    path('savat_k/<int:id>/', AyirView.as_view()),
    path('ochirish/<int:id>/', OchirView.as_view()),
    path('qoshish/<int:id>/', QoshishView.as_view()),
    path('tanlangan_qoshish/<int:id>/', TanlanganQoshishView.as_view()),
    path('tanlangan_ochirish/<int:id>/', TanlanganDeleteView.as_view()),
    path('wish_ochirish/<int:id>/', TanlanganDeleteView.as_view()),
    path('wishlist/', WishlistView.as_view()),
]