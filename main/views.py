from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/home.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def security_info(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 15)  # 페이지당 15개의 게시글
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/security_info.html', {'page_obj': page_obj, 'is_paginated': page_obj.has_other_pages()})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        # 게시글 작성 처리 로직 추가
        pass
    return render(request, 'main/post_create.html')
def function2(request):
    return render(request, 'main/function2.html')

def function3(request):
    return render(request, 'main/function3.html')

def function4(request):
    return render(request, 'main/function4.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'