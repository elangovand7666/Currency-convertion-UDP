from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from convertingAPI.udpclient import re


def index(request):
    if(request.method=='GET'):
        return render(request,'index.html')
    if(request.method=='POST'):
        cur=request.POST.get('amount')
        f=request.POST.get('from_currency')
        t=request.POST.get('to_currency')
        t1=re(cur,f,t)
        print(t1)
        return render(request,'login.html',{'t1':t1})
    
        
        

