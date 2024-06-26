from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import SignUpForm, PostForm
from .models import Post, Category

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'categories': categories})

from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator

def board(request):
    category_id = request.GET.get('category')
    if category_id:
        posts = Post.objects.filter(category_id=category_id).order_by('-created_at')
        category = get_object_or_404(Category, id=category_id)
        category_name = category.name
    else:
        posts = Post.objects.all().order_by('-created_at')
        category_name = "모아보기"

    paginator = Paginator(posts, 15)  # 페이지당 15개의 게시물 표시
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    categories = Category.objects.filter(type='board')
    
    return render(request, 'main/board.html', {
        'posts': posts,
        'categories': categories,
        'category_name': category_name,
        'category_id': category_id,
        'total_posts': paginator.count,
    })

def security_news(request):
    category_id = request.GET.get('category', None)
    category_name = "보안뉴스"
    
    if category_id:
        posts = Post.objects.filter(category_id=category_id, category__type='news').order_by('-created_at')
        category = Category.objects.get(id=category_id)
        category_name = category.name
    else:
        posts = Post.objects.filter(category__type='news').order_by('-created_at')
    
    paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    categories = Category.objects.filter(type='news')
    total_posts = paginator.count
    return render(request, 'main/security_news.html', {
        'posts': posts,
        'categories': categories,
        'category_id': category_id,
        'total_posts': total_posts,
        'category_name': category_name
    })

@login_required
def create_post(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.category = category
            post.save()
            if category.type == 'board':
                return redirect(f'/board/?category={category_id}')
            else:
                return redirect(f'/security-news/?category={category_id}')
    else:
        form = PostForm()

    categories = Category.objects.filter(type=category.type)
    return render(request, 'main/create_post.html', {'form': form, 'categories': categories, 'category': category})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.username != post.author:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            if post.category.type == 'board':
                return redirect(f'/board/?category={post.category.id}')
            else:
                return redirect(f'/security-news/?category={post.category.id}')
    else:
        form = PostForm(instance=post)
    
    categories = Category.objects.filter(type=post.category.type)
    return render(request, 'main/edit_post.html', {'form': form, 'categories': categories, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.username != post.author:
        return HttpResponseForbidden()
    
    category_id = post.category.id
    category_type = post.category.type
    post.delete()
    if category_type == 'board':
        return redirect(f'/board/?category={category_id}')
    else:
        return redirect(f'/security-news/?category={category_id}')

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
    post.views += 1
    post.save()

    if post.category.type == 'board':
        categories = Category.objects.filter(type='board')
        posts = Post.objects.filter(category__type='board').order_by('-created_at')
    else:
        categories = Category.objects.filter(type='news')
        posts = Post.objects.filter(category__type='news').order_by('-created_at')

    paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    total_posts = paginator.count

    return render(request, 'main/post_detail.html', {
        'post': post,
        'categories': categories,
        'posts': posts,
        'total_posts': total_posts,
        'category_type': post.category.type
    })

def logout_view(request):
    logout(request)
    return redirect('index')
