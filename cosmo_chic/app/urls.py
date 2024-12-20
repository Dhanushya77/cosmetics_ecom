from django.urls import path
from . import views

urlpatterns = [
    # --------shop-------------------
    path('',views.cosmetic_login),
    path('logout',views.cosmetic_logout),
    path('shop_home',views.shop_home),

    # -----------user-----------------------
    path('register/',views.register),
    path('user_home',views.user_home),
]