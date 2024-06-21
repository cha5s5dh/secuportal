from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'main/home.html')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/home.html')

def security_info(request):
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 15)  # 한 페이지에 15개의 게시글
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    }
    return render(request, 'main/security_info.html', context)

def post_create(request):
    if request.method == 'POST':
        Post.objects.create(
            category=request.POST['category'],
            title=request.POST['title'],
            author=request.POST['author'],
            content=request.POST['content'],
            views=0
        )
        return redirect('security_info')
    return render(request, 'main/post_create.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    return render(request, 'main/post_detail.html', {'post': post})

def function2(request):
    return render(request, 'main/function2.html')

def function3(request):
    return render(request, 'main/function3.html')

def function4(request):
    return render(request, 'main/function4.html')
