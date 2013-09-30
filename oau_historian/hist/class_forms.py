#from django import forms
from django.forms import ModelForm
from hist.models import config, tag 

class ConfigForm(ModelForm):
    class Meta:
        model = config
        #fields = ('username', 'first_name', 'last_name', 'email')
        
class TagForm(ModelForm):
    class Meta:
        model = tag