from django.urls import path
from .import views
from management import urls

urlpatterns = [
    path('addclass',views.AddClasses.as_view(),name='Addclass'),
    path('classlist',views.classlist,name='classlist'),
    #path('', views.home, name='home'),
    
    
]