from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, PostForm
from .models import Post, Category
from django.core.paginator import Paginator  # Paginator 임포트 추가

def index(request):
    posts = Post.objects.all()[:5]  # 메인 페이지에 표시할 게시물 5개
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'categories': categories})

def board(request):
    category_id = request.GET.get('category', None)
    posts = Post.objects.all()
    if category_id:
        posts = posts.filter(category_id=category_id)
    
    paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    categories = Category.objects.all()
    return render(request, 'main/board.html', {'posts': posts, 'categories': categories})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.save()
            return redirect('board')
    else:
        form = PostForm()
    
    categories = Category.objects.all()
    return render(request, 'main/board.html', {'form': form, 'categories': categories, 'is_create_page': True})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = Post.objects.all().order_by('-created_at')  # 보안 게시판의 모든 게시글
    categories = Category.objects.all()
    return render(request, 'main/post_detail.html', {'post': post, 'posts': posts, 'categories': categories})
