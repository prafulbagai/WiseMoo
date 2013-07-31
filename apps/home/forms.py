from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.data.models import *

class DocumentForm(forms.Form):
    
    docfile = forms.ImageField(
        label='Select a file',
        
    )
    
class RegisterForm(UserCreationForm):
    name     = forms.CharField()
    phone    = forms.IntegerField() 
    gender   = forms.ChoiceField(choices=WisemooUser.GENDER)
    
    def save(self, *args, **kwargs):
        user = super(RegisterForm,self).save(*args,**kwargs)
        
        WisemooUser.objects.create(user=user , gender=self.cleaned_data['gender'], name = self.cleaned_data['name'], phone = self.cleaned_data['phone'])
        
        return user