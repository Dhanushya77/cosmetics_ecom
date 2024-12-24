from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.models import *
import os
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def cosmetic_login(req):
    if 'shop' in req.session:
        return redirect (shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method == 'POST':
        uname = req.POST['uname']
        password = req.POST['password']
        shop = authenticate(username=uname,password=password)
        if shop:
            login(req,shop)
            if shop.is_superuser:
                req.session['shop'] = uname
                return redirect(shop_home)
            else:
                req.session['user'] = uname
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password')
            return redirect(cosmetic_login)
    else:
        return render(req,'login.html')
    

#-----------------admin----------------------------------------


def cosmetic_logout(req):
    logout(req)
    req.session.flush()
    return redirect(cosmetic_login)

def shop_home(req):
    if 'shop' in req.session:
        products = product.objects.all()
        return render(req,'shop/home.html',{'product':products})
    else:
        return redirect(cosmetic_login)
    
def details(req):
    if req.method=='POST':
        pro=req.POST['pid']
        price=req.POST['price']
        offer_price=req.POST['offer_price']
        stock=req.POST['stock']
        weight=req.POST['weight']
        data=Details.objects.create(price=price,offer_price=offer_price,stock=stock,weight=weight,product=product.objects.get(pid=pro))
        data.save()
        return redirect(shop_home)

    else:
        data=product.objects.all()
        return render(req,'shop/details.html',{'data':data})
    
def category(req):
    if req.method=='POST':
        category=req.POST['category']
        data= Category.objects.create(category=category)
        data.save()
        return redirect(shop_home)
    else:
        data=Category.objects.all()
        return render(req,'shop/category.html',{'data':data})
    
def add_pro(req):
    if 'shop' in req.session:
        if req.method == 'POST':
            pid = req.POST['pid']
            name = req.POST['name']
            dis = req.POST['dis']
            category = req.POST['category']
            img = req.FILES.get('img')
            data = product.objects.create(pid=pid,name=name,dis=dis,category=Category.objects.get(category=category),img=img)
            data.save()
            return redirect(details)
        else:
            data=Category.objects.all()
            return render(req,'shop/add_pro.html',{'data':data})
    else:
        return redirect(cosmetic_login)
    
    
def edit_pro(req, id):
    if req.method == 'POST':
        pid = req.POST['pid']
        name = req.POST['name']
        dis = req.POST['dis']
        price = req.POST['price']
        offer_price = req.POST['offer_price']
        stock = req.POST['stock']
        weight = req.POST['weight']
        img = req.FILES.get('img')
        
        if img:
            product.objects.filter(pk=id).update(pid=pid, name=name, dis=dis)
            data = product.objects.get(pk=id)
            data.img = img
            data.save()
        else:
            product.objects.filter(pk=id).update(pid=pid, name=name, dis=dis)
        
        Details.objects.filter(pk=id).update(price=price, offer_price=offer_price, stock=stock,weight=weight)
        return redirect(shop_home)
    else:
        product_data = product.objects.get(pk=id)
        details_data = Details.objects.get(pk=id)
        return render(req, 'shop/edit_pro.html', {'product_data': product_data, 'details_data': details_data})

    
def delete_pro(req,pid):
    data=product.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)



# -----------------user---------------------------------------------

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswrd=req.POST['pswrd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswrd)
            data.save()
            send_mail('Registration','Your registration completed', settings.EMAIL_HOST_USER, [email])
            return redirect(cosmetic_login)
        except:
            messages.warning(req,'Email already exist')
            return redirect(cosmetic_login)
    else:
        return render(req,'user/register.html')
    
def user_home(req):
    if 'user' in req.session:
        products = product.objects.all()
        return render(req,'user/home.html',{'product':products})
    else:
        return redirect(cosmetic_login)


