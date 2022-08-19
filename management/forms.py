from django import forms;
from .models import *

class AddsubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields="__all__"

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields="__all__"

class DeleteForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields="__all__"
