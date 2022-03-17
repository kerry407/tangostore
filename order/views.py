from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from home.models import Setting
from product.models import Category, Product
from .models import ShopCart, ShopCartForm,Order, OrderForm
from  user.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
import json
import random
import string
import uuid
from django.views.decorators.http import require_POST
from django.conf import settings




@require_POST
@login_required(login_url='login')
def addtoshopcart(request):
    url = request.META.get('HTTP_REFERER')
    thequantity = int(request.POST['quantity'])
    thesize = request.POST.get('size', None)
    theprodid = request.POST['prodid']
    aprod = Product.objects.get(pk=theprodid)

     #check if the user has an existing cart
    cart = ShopCart.objects.filter(order_placed=False).filter(user__username = request.user.username)

    if cart: #an existing cart is noticed
        prodchecker = ShopCart.objects.filter(product_id = aprod.id, size=thesize, quantity=thequantity,user__username = request.user.username).first()
        
        if prodchecker: #product exists in the cart, increment it
            prodchecker.quantity += thequantity
            prodchecker.size = thesize
            prodchecker.save()
            messages.success(request, "Product added to Shopcart")
            return redirect(url)

        else: #product is not in the cart, add it
            anitem = ShopCart()
            anitem.product=aprod
            anitem.user=request.user
            anitem.order_code=cart[0].order_code
            anitem.quantity=thequantity
            anitem.size= thesize
            anitem.order_placed=False
            anitem.save()                
                 
        
    else: #create a new cart, generate  order code
        ordercode = str(uuid.uuid4())
        newcart = ShopCart()
        newcart.product=aprod
        newcart.user=request.user
        newcart.order_code=ordercode
        newcart.quantity=thequantity
        newcart.size= thesize
        newcart.order_placed=False
        newcart.save()

    messages.success(request, "Product added to Shopcart")

    return redirect(url)



@login_required(login_url='login')
def shopcart(request):  
    category = Category.objects.all() 
    setting= Setting.objects.get(pk=1)
    shopcart = ShopCart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    
    subtotal=0
    shippingfee = 0
    vat =0
    total = 0
    
    for item in shopcart:
        if item.product.discount_price:
            subtotal += item.product.discount_price * item.quantity
        else:
            subtotal += item.product.price * item.quantity

    # Shipping rules: 8% fees to all orders above 150. 0 fees to orders lower
    if subtotal > 150:
        shippingfee = 0.08 * subtotal
    else:
        shippingfee = 0

    vat = 0.075 * subtotal

    total = subtotal + shippingfee + vat
   
    
    context = { 
                'setting': setting,
                'category': category,
                'shopcart': shopcart,
                'subtotal': subtotal,
                'shipping': shippingfee,
                'vat': vat,
                'total':total
                 }

    return render(request, 'shopcart.html', context)



@require_POST
@login_required(login_url='login')
def updatequantity(request):
    url = request.META.get('HTTP_REFERER')
    newquantity = request.POST['itemquantity']
    theitem = ShopCart.objects.get(id=request.POST['itemid'])
    theitem.quantity = newquantity
    theitem.save()

    messages.success(request, "Product Quantity successfully updated")
    return redirect(url)



@login_required(login_url='login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Item deleted from Shopcart.')
    return redirect('order:shopcart')


@login_required(login_url='login')
def checkout(request):
    category = Category.objects.all()  
    setting= Setting.objects.get(pk=1)
    shopcart = ShopCart.objects.filter(user__username = request.user.username).filter(order_placed=False)
    profile= UserProfile.objects.get(user__username = request.user.username)

    subtotal=0
    shippingfee = 0
    vat = 0
    total = 0

    for item in shopcart:
        if item.product.discount_price:
            subtotal += item.product.discount_price * item.quantity
        else:
            subtotal += item.product.price * item.quantity 

    # Shipping rules: 8% fees to all orders above 150. 0 fees to orders lower
    if subtotal > 150:
        shippingfee = 0.08 * subtotal
    else:
        shippingfee = 0

    # vat is at 7.50% of the total purchase to  be made 
    vat = 0.075 * subtotal

    total = subtotal + shippingfee + vat    

    context = { 
                'setting': setting,                
                'shopcart': shopcart,
                'order_code': shopcart[0].order_code,
                'profile': profile,
                'category': category,               
                'subtotal': subtotal,
                'shipping': shippingfee,
                'vat': vat,
                'total':total
                 }
    return render(request, 'checkout.html', context)
    


@require_POST
@login_required(login_url='login')
def placeorder(request):
    api_key = settings.API_KEY
    url = 'https://api.paystack.co/transaction/initialize'
    callback_url = 'http://localhost:8000/order/ordercompleted/'
    ordercode =  request.POST['order_number']
    autogen_ref = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
    current_user = User.objects.get(username = request.user.username)
    user = UserProfile.objects.get(user_id = current_user.id)
    total = float(request.POST['amount']) * 100    
    

    headers = {'Authorization': f'Bearer {api_key}'}
    data = {'reference': autogen_ref, 'amount':int(total), 'order_number':ordercode, 'email':user.email, 'callback_url':callback_url }

    
    # making a request to PAYSTACK 
    try:
        r = requests.post(url, headers=headers, json=data)
    except Exception:
        messages.error(request, 'Network busy. Please try again in few minutes. Thank You!')
    else:
        # create an order 
        transback = json.loads(r.text)
        
        rd_url = transback['data']['authorization_url']
        theuser= UserProfile.objects.filter(user=request.user).first()
        order = Order()
        order.first_name=theuser.user.first_name
        order.last_name=theuser.user.last_name
        order.phone=theuser.phone
        order.city=theuser.city
        order.order_code= ordercode
        order.payment_code = autogen_ref
        order.total=total
        order.order_placed = True
        order.save()
        return redirect(rd_url)
    return redirect('order:checkout')



@login_required(login_url='login')
def ordercompleted(request):
    category = Category.objects.all()  
    setting= Setting.objects.get(pk=1)
    offer = Product.objects.get(offer=True)
    profile= UserProfile.objects.get(user__username = request.user.username)
    shopcart = ShopCart.objects.filter(order_placed=False).filter(user__username = request.user.username)
    
    #cleaning the shopcart
    for item in shopcart:
        item.order_placed = True
        item.save()
    
    
        #reducing quantity instock
        aproduct = Product.objects.get(id=item.product.id)
        aproduct.quantity_instock -= item.quantity
        aproduct.save() 


    context = {
                'setting': setting,
                'offer': offer,
                'category': category,
                'shopcart': shopcart,
                'profile': profile,
    }
    
    return render(request, 'ordercompleted.html', context)
