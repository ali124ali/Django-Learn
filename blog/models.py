from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'images', default = 'default.jpg')
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    # tag
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        # app_label = 'blog'
        ordering = ['created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'
        
    def __str__(self):
        return "{}->{}".format(self.id, self.title)

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})