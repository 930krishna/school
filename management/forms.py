from django.forms import *
from .models import *

class AddsubjectForm(ModelForm):
    class Meta:
        model=Subject
        fields="__all__"