from django.contrib.auth.models import User
from .models import Image
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

class UploadFileForm(forms.ModelForm):        
    title = forms.CharField(max_length=50)
    keyword1 = forms.CharField(max_length=50)
    keyword2 = forms.CharField(max_length=50)
    keyword3 = forms.CharField(max_length=50)
    photo = forms.ImageField()
    
    class Meta:
        model = Image
        fields = ['title', 'keyword1', 'keyword2', 'keyword3', 'photo']
        exclude = ["user"]