from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name = 'home'),
    path('category/<str:cat_name>', blog, name='category'),
    path('tag/<str:tag_name>', blog, name='tag'),
    path('author/<str:author_username>', blog, name='author'),
    path('search/', search, name='search'),
    path('<int:pid>', blog_single, name = 'single'),
    path('test/', test)
]

