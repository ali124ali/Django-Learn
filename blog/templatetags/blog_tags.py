from django import template
from blog.models import Post, Category, Comment
from datetime import datetime

register = template.Library()

# @register.simple_tag(name="posts")  
# def hello():
#     posts = Post.objects.filter(status=1)
#     return (posts)

# @register.filter
# def snippet(value, count):
#     return value[:count]

@register.inclusion_tag('blog/blog-popularposts.html')
def popularPosts(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-counted_view')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()

    countcat = {}
    for cat in categories:
        countcat[cat] = posts.filter(category=cat).count()

    return {'categories':  countcat}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post = pid, approved=True).count()
     
