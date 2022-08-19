from http.client import HTTPResponse
from re import search
from this import s
from django.shortcuts import render,redirect,get_object_or_404
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

# def subList(request):
#     data=Subject.objects.all()

#     # creating a paginator object
#     p = Paginator(data, 5)

#     # getting the desired page number from url
#     page_number = request.GET.get('page')

#     # returns the desired page object
#     page_obj = p.get_page(page_number) 

#     return render(request,'subList.html', {'mydata': page_obj})              

class SubList(View):
    def get(self,request):
        data=Subject.objects.all()
        # creating a paginator object
        p = Paginator(data, 5)

        # getting the desired page number from url
        page_number = request.GET.get('page')

        # returns the desired page object
        page_obj = p.get_page(page_number) 
        return render(request,'subList.html', {'mydata': page_obj})              
    def post(self,request):
        subject = request.POST['subject']
        if subject:
            data = Subject.objects.filter(subject_name__exact=subject)
        else:
            data = Subject.objects.all() 
        # creating a paginator object
        p = Paginator(data, 5)

        # getting the desired page number from url
        page_number = request.GET.get('page')

        # returns the desired page object
        page_obj = p.get_page(page_number) 
        return render(request,'subList.html', {'mydata': page_obj, 'subject': subject})

class SearchSub(View):
    def get(self,request):
        return render(request,'subname.html')
    def post(self,request):
        ssearch=request.POST['search']
        sname=request.POST['sub']
        if(ssearch and sname):
            data=Subject.objects.filter(sname__exact='sub').filter(ssearch__exact=search)
        else:
            return render(request,'search.html')



class UpdateSub(View):
    def get(self,request,id):
        obj=get_object_or_404(Subject,id=id)
        myform=UpdateForm(instance=obj)
        return render(request,'updsub.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Subject,id=id)
        myform=UpdateForm(request.POST,instance=obj)
        if myform.is_valid():
            myform.save()
            return redirect('subList')

class DeleteSub(View):
    def get(self,request,id):
        obj=get_object_or_404(Subject,id=id)
        myform=DeleteForm(instance=obj)
        return render(request,'delsub.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Subject,id=id)
        obj.delete()
        return redirect('subList')               


            
        

                 



