from django.shortcuts import render

def login(request):
    return render(request,"customer/login.html")

def register(request):
    return render(request,"customer/register.html")
