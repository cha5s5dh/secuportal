from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'main/home.html')

def security_info(request):
    posts = Post.objects.all()
    return render(request, 'main/security_info.html', {'posts': posts})

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
