from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *

def home(request):
    return render(request,'home.html')

class AddSubject(View):
    def get(self,request):
        myform=AddsubjectForm()
        return render(request,'addsubject.html',{'myform':myform})
    def post(self,request):
        myform=AddsubjectForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('home')
        else:
            return HTTPResponse("<h4>Subject is not added.</h4>")    

