from django.forms import ModelForm
from .models.todo import TODO

class todoform(ModelForm):
    class Meta:
        model=TODO
        fields=['title','status','priority']
        
    