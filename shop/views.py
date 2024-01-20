from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
from math import ceil
from django.contrib import messages

def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,(1,nSlides),nSlides])

    params = {'allProds': allProds}
    return render (request, "shop/index.html", params)

def about(request):
    return render (request, "shop/about.html")

def contact(request):
    if request.method == "POST" :
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone =  request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, "Your message has been Sent Successfully.")
    return render (request, "shop/contact.html")

def tracker(request):
    return render (request, "shop/tracker.html")

def productView(request,myid):
    product = Product.objects.filter(id=myid)
    # print(product)
    return render (request, "shop/products.html",{'product':product[0]})

def search(request):
   return render (request, "shop/search.html")

def checkout(request):
    if request.method == "POST" :
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        phone =  request.POST.get('phone','')
        # print(desc)
        order = Order(name=name,email=email,address=address,city=city,state=state,phone=phone,items_json= items_json)
        order.save()
        thank = True
        id = order.order_id
        return render (request, "shop/checkout.html",{'thank':thank, 'id':id})
    return render (request, "shop/checkout.html")
