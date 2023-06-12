from django import template
from blog.models import  Post
from datetime import datetime

register = template.Library()

@register.inclusion_tag('website/home-recent-posts.html')
def recent_posts(arg=6):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')[:arg]

    return {'posts':posts}
