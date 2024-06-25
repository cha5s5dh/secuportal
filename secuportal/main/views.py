from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, PostForm
from .models import Post, Category

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'categories': categories})

def board(request):
    category_id = request.GET.get('category', None)
    posts = Post.objects.all().order_by('-created_at')
    category_name = "보안 게시판"
    if category_id:
        posts = posts.filter(category_id=category_id)
        category = Category.objects.get(id=category_id)
        category_name = category.name
    
    paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    categories = Category.objects.all()
    total_posts = paginator.count
    return render(request, 'main/board.html', {'posts': posts, 'categories': categories, 'category_id': category_id, 'total_posts': total_posts, 'category_name': category_name})

@login_required
def create_post(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.category = category  # 카테고리를 폼에서 설정
            post.save()
            return redirect(f'/board/?category={category_id}')
    else:
        form = PostForm()

    categories = Category.objects.all()
    return render(request, 'main/create_post.html', {'form': form, 'categories': categories, 'category': category})

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
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    total_posts = paginator.count
    return render(request, 'main/post_detail.html', {'post': post, 'categories': categories, 'posts': posts, 'total_posts': total_posts})

def logout_view(request):
    logout(request)
    return redirect('index')
