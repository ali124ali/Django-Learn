from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime

def blog(request, **kwargs):
    posts = Post.objects.filter(status = 1, published_date__lte=datetime.now()).order_by('id')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
        
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post,status = 1,id=pid)
    posts = list(Post.objects.filter(status = 1, published_date__lte=datetime.now()).order_by('id'))

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
        
        
def test(request):
    return render(request, 'blog/test.html')


