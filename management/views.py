from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .froms import *
# Create your views here.


class AddClasses(View):
    def get(self,request):
        myform=AddClassform()
        return render(request,'Addcls.html',{'myform':myform})
    
    def post(self,request):
        myform=AddClassform(request.POST)
        if myform.is_valid():
            myform.save()
            return HttpResponse("<h1>class Added..")
        else:
            return HttpResponse("<h5>Data could not be added")



def classlist(request):
    data=AddClass.objects.all()
    return render(request,'classlist.html',{'mydata':data})
    
    
    
