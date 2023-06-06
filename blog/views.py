from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime

def blog(request):
    posts = Post.objects.filter(status = 1, published_date__lte=datetime.now())
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post,status = 1,id=pid)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    post = get_object_or_404(Post,id=pid)
    context = {'post':post}
    return render(request, 'blog/test.html', context)


