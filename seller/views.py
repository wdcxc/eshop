from django.shortcuts import render

def login(request):
    return render(request,"seller/login.html",{"hi":"seller"})
