# main/views.py

from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'main/home.html')

def security_info(request):
    posts = Post.objects.all()
    return render(request, 'main/security_info.html', {'posts': posts})

def function2(request):
    return render(request, 'main/function2.html')

def function3(request):
    return render(request, 'main/function3.html')

def function4(request):
    return render(request, 'main/function4.html')
