from django import template
from blog.models import Post
from datetime import datetime

register = template.Library()

@register.simple_tag(name="posts")  
def hello():
    posts = Post.objects.filter(status=1)
    return (posts)

@register.filter
def snippet(value, count):
    return value[:count]

@register.inclusion_tag('blog/blog-popularposts.html')
def popularPosts(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-counted_view')[:arg]
    return {'posts':posts}