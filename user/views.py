from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from home.models import Setting
from product.models import Category, Product
from .decorators import unauthenticated_user
 
# Create your views here.


def user(request):
    return HttpResponse('user running..')

@unauthenticated_user
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            myuser = form.save()
            p = UserProfile(user=myuser)
            p.first_name = myuser.first_name
            p.last_name = myuser.last_name
            p.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account for {email} has been created, you can now log in and shop with us')
            return redirect('login')
        else:
            messages.error(request, form.errors)
    else:
        form = UserRegisterForm()

    setting = Setting.objects.get(pk=1)

    context = {
        'form': form,
        'setting': setting
    }

    return render(request, 'register.html', context)

@unauthenticated_user
def loginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, f'Username Or Password is incorrect')
        
    setting = Setting.objects.get(pk=1)

    context = {
        'setting': setting
    }

    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userprofile(request):
        
    setting = Setting.objects.get(pk=1)
    category= Category.objects.all()
    offer= Product.objects.get(offer=True)
    profile= UserProfile.objects.filter(user_id=request.user.id).first()

    context = {
        'setting': setting,
        'category': category,
        'profile': profile,
        'offer': offer,
    }

    return render(request, 'userprofile.html', context)


@login_required(login_url='login')
def userupdate(request):
    if request.method == 'POST':
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profileform.is_valid:
            profileform.save()
            messages.success(request, f'Your Account has been updated')
            return redirect('userprofile')
        else:
            messages.warning(request, profileform.errors)
            return redirect('userupdate')
    else:
        profileform = ProfileUpdateForm(instance=request.user.userprofile)
        
    setting = Setting.objects.get(pk=1)
    category= Category.objects.all()
    offer= Product.objects.get(offer=True)
    profile= UserProfile.objects.filter(user_id=request.user.id).first()

    context = {
        'profileform': profileform,
        'setting': setting,
        'category': category,
        'profile': profile,
        'offer': offer,
    }

    return render(request, 'userupdate.html', context)
