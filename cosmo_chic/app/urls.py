from django.urls import path
from . import views

urlpatterns = [
    # --------shop-------------------
    path('',views.cosmetic_login),
    path('logout',views.cosmetic_logout),
    path('shop_home',views.shop_home),
    path('add_pro',views.add_pro),
    path('details',views.details),
    path('category',views.category),
    path('edit_pro/<id>',views.edit_pro),
    path('delete_pro/<pid>',views.delete_pro),
    

    # -----------user-----------------------
    path('register/',views.register),
    path('user_home',views.user_home),
]