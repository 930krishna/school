from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
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
            messages.success(request, "Subject Added Successfully")
            return redirect('subList')
        else:
            return HTTPResponse("<h4>Subject is not added.</h4>")    

def subList(request):
    data=Subject.objects.all()

    # creating a paginator object
    p = Paginator(data, 5)

    # getting the desired page number from url
    page_number = request.GET.get('page')

    # returns the desired page object
    page_obj = p.get_page(page_number) 

    context = {'mydata': page_obj}
    return render(request,'subList.html',context)              

