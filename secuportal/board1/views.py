from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.utils.dateparse import parse_datetime

CATEGORY_NAMES = {
    'temp1': '보안뉴스',
    'temp2': '보안가이드',
    'temp3': '임시3',
    'temp4': '임시4'
}

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'home.html', {
        "latest_posts": latest_posts,
    })

def board1_index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'board1/board1_index.html', {
        "page_obj": page_obj,
        "show_create": True  # 글쓰기 버튼을 표시
    })

def post_list(request, category):
    posts = Post.objects.filter(category=category).order_by('-created_at')
    total_posts = posts.count()
    
    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    start_index = total_posts - (page_obj.start_index() - 1)

    category_name = CATEGORY_NAMES.get(category, 'Unknown')

    return render(request, 'board1/post_list.html', {
        "page_obj": page_obj,
        "category": category_name,
        "category_key": category,
        "total_posts": total_posts,
        "start_index": start_index,
        "show_create": True  # 글쓰기 버튼을 표시
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.views += 1
    post.save()
    
    related_posts = Post.objects.filter(category=post.category).exclude(id=post_id).order_by('-created_at')[:10]
    category_posts = Post.objects.filter(category=post.category).order_by('-created_at')
    total_posts = category_posts.count()
    
    paginator = Paginator(category_posts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    start_index = total_posts - (page_obj.start_index() - 1)

    category_name = CATEGORY_NAMES.get(post.category, 'Unknown')

    return render(request, 'board1/post_detail.html', {
        "post": post,
        "related_posts": related_posts,
        "page_obj": page_obj,
        "category_name": category_name,
        "total_posts": total_posts,
        "start_index": start_index
    })

def create_post(request, category):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.category = category  # URL에서 받은 카테고리 값을 사용
            new_post.author = "임시 작성자"  # 임시 작성자 지정
            original_time = form.cleaned_data.get('original_time')
            if original_time:
                new_post.original_time = original_time
            new_post.save()
            return redirect('post_list', category=category)
    else:
        form = PostForm()
    return render(request, 'board1/create_post.html', {"form": form, "category_key": category})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'board1/edit_post.html', {"form": form, "post": post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('board1_index')
    return render(request, 'board1/post_detail.html', {"post": post})
