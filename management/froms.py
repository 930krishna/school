# from pyexpat import model
from django import forms
from .models import *
#from dataclasses import fields

class AddClassform(forms.ModelForm):
    class Meta:
        model=AddClass
        fields="__all__"
        
