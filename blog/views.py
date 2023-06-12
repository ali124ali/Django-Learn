from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request, **kwargs):
    posts = Post.objects.filter(status = 1, published_date__lte=datetime.now()).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    
    posts = Paginator(posts, 3)
    
    try:
        page_num = request.GET.get('page')
        posts = posts.get_page(page_num)

    except PageNotAnInteger:
        posts = posts.page(1)

    except EmptyPage:
        posts = posts.page(posts.num_pages)

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post,status = 1,id=pid)
    posts = list(Post.objects.filter(status = 1, published_date__lte=datetime.now()))

    index = posts.index(post)

    if index == 0:
        next_post = posts[index + 1]
        prev_post = None

    elif index == len(posts) - 1:
        prev_post = posts[index - 1]
        next_post = None

    else:
        prev_post = posts[index - 1]
        next_post = posts[index + 1]

    context = {'post':post, 'prev':prev_post, 'next':next_post}

    def counter():
        post.counted_view += 1
        post.save()

    counter()
    return render(request, 'blog/blog-single.html', context)
        
def search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)

    content = {'posts':posts}
    return render(request, 'blog/blog-home.html', content)    


def test(request):
    return render(request, 'blog/test.html')


