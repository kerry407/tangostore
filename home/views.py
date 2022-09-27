from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from product.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from product.filters import ProductFilter
# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    brand = Brand.objects.all()
    category = Category.objects.all()[:4]
    offer = Product.objects.get(offer=True)
    category1 = Product.objects.filter(featured=True).order_by('-id')[:4]
    about = About.objects.get(pk=1)
    offer1 = Product.objects.filter(offer=True)

    context = {
        'setting': setting,
        'brand': brand,
        'category': category,
        'offer': offer,
        'category1': category1,
        'about': about,
        'offer1': offer1,
    }
    return render(request,'index.html', context)



def category(request):
    offer = Product.objects.get(offer=True)
    category = Category.objects.all()
    category1 = Product.objects.filter(featured=True).order_by('-id')[:4]
    categorys = Category.objects.get(pk=1)
    paginator = Paginator(category, 4)
    page = request.GET.get('page')
    paged_category = paginator.get_page(page)
   

    context = {
        'offer': offer,
        'category1': category1,
        'category': paged_category,
        'categorys': categorys,

       
    }

    return render(request, 'category.html', context)



def prod_list(request, id):

    category = Category.objects.all()
    catdata = Category.objects.get(pk=1)
    products = Product.objects.filter(category_id=id)
    category1 = Product.objects.filter(featured=True).order_by('-id')[:4]
    products2 = Product.objects.filter(category_id=id).order_by('-id')[:4]
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_category = paginator.get_page(page)
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    product = Product.objects.filter(category_id=id)[:1]
    offer1 = Product.objects.filter(offer=True)

    context = {
      
        'category': category,
        'catdata': catdata,
        'products': products,
        'product': product,
        'products2': products2,
        'category1': category1,
        'page': page,
        'paged_category': paged_category,
        'myFilter': myFilter,
        'offer1': offer1
        
    }

    return render(request, 'product.html', context)




def prod_detail(request, id):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    product = Product.objects.get(pk=id)

    context = {
        'category': category,
        'products': products,
        'product': product,
      
    }

    return render(request, 'products-details.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message has been sent! Our Customer Service Team will reach you soon.")
            return redirect('contact')


    setting = Setting.objects.get(pk=1)
    form = ContactForm
    brands = Brand.objects.all()
    category = Category.objects.all()
    about = About.objects.get(pk=1)
       
    context= { 'setting': setting,
                'form': form,
                'brands': brands,
                'category': category,
                'about': about,
    }

    return render(request, 'contact.html', context)