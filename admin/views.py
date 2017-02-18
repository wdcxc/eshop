from django.shortcuts import render

def login(request):
    return render(request,"admin/login.html",{"hi":"admin"})
