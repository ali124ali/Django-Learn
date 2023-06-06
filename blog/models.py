from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'images', default = 'default.jpg')
    # category
    # tag
    counted_view = models.IntegerField(default=0)
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