from django.shortcuts import render

def login(request):
    return render(request,"customer/login.html",{"hi":"customer"})
