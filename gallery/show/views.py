from django.shortcuts import render, redirect
from .models import Image
from .forms import UserForm, UploadFileForm
from django.db.models import Q
from django.contrib.auth import authenticate,login, logout
from django.views.generic import View as view

# Create your views here.
def show_random_images(request):
        image_list = Image.objects.all().order_by('?')[:30]
        return render(request, 'show/show_random_images.html', {'image_list': image_list})
    
def show_index(request):
    if request.user.is_authenticated():
        image_list = Image.objects.filter(user=request.user)
        return render(request, 'show/index_page.html', {'image_list': image_list})
    else:
        return render(request, 'show/index_page.html', {})
    
def delete(request, delete):
    if request.user.is_authenticated:
        delete = delete.replace("/", "")
        image = Image.objects.filter(id=delete)
        image.delete()
    return redirect('show_index') 
    
def search(request, search):
    search = search.replace("/", "")
    if "," not in search: 
        searched_images = Image.objects.filter(Q(keyword1__contains=search) | Q(keyword2__contains=search) | Q(keyword3__contains=search))[:30]
    else:
        search = search.split(',')
        if len(search) == 2:
            searched_images = Image.objects.filter(Q(keyword1__contains=search[0]) | Q(keyword2__contains=search[0]) | Q(keyword3__contains=search[0]) | Q(keyword1__contains=search[1]) | Q(keyword2__contains=search[1]) | Q(keyword3__contains=search[1]))[:30]
        elif len(search) == 3:
            searched_images = Image.objects.filter(Q(keyword1__contains=search[0]) | Q(keyword2__contains=search[0]) | Q(keyword3__contains=search[0]) | Q(keyword1__contains=search[1]) | Q(keyword2__contains=search[1]) | Q(keyword3__contains=search[1]) | Q(keyword1__contains=search[2]) | Q(keyword2__contains=search[2]) | Q(keyword3__contains=search[2]))[:30]
        else:
            redirect('show:index_page')
    
    return render(request, 'show/show_searched_images.html', {'image_list': searched_images})

def unsplash(request):
    return render(request, 'unsplash/index.html', {})
  
def logoutu(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')
    return redirect('/')

class UploadView(view):
    form_class = UploadFileForm
    template_name = 'show/upload.html'
    
    def get(self,request):
        if request.user.is_authenticated:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})
        return redirect('show_index')
    
    def post(self,request):        
        form = self.form_class(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            title = form.cleaned_data['title']
            keyword1 = form.cleaned_data['keyword1']
            keyword2 = form.cleaned_data['keyword2']
            keyword3 = form.cleaned_data['keyword3']
            photo = form.cleaned_data['photo']
            uploading = form.save(commit=False)
            uploading.user = request.user 
            uploading.save()
                
        return redirect('show_index')
    
class UserFormView(view):
    form_class = UserForm
    template_name = 'show/registration.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.set_password(password)
            user.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('show_index')
                
        return render(request, self.template_name, {'form': form})
    
class UserCheck(view):
    template_name = 'show/login.html'
    
    def get(self,request):
        return render(request, self.template_name, {'error': False})
    
    def post(self,request):
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('show_index')
                
        return render(request, self.template_name, {'error': True})