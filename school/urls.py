"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from re import search
from django.contrib import admin
from django.urls import path,include
from . import views
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('management',include('management.urls')),

    # CRUD operation for subject
    path('addsub',views.AddSubject.as_view(),name='addsub'),
    path('subList',views.SubList.as_view(),name='subList'),
    path('SearchSub',views.SearchSub.as_view(),name='searchsub'),
    path('updsub<id>',views.UpdateSub.as_view(),name='updsub'),
    #path('delsub/<id>',views.DeleteSub.as_view(),name='delsub'),
]
