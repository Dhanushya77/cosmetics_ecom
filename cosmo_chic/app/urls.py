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
    path('view_category',views.view_category),
    path('delete_category/<id>',views.delete_category),
    path('view_products/<id>',views.view_products),
    path('edit_pro/<id>',views.edit_pro),
    path('delete_pro/<pid>',views.delete_pro),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    

    # -----------user-----------------------
    path('register/',views.register),
    path('otp',views.otp_confirmation),
    path('user_home',views.user_home),
]