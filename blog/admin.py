from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '????'
    list_display = ('title','author', 'counted_view', 'status', 'updated_date', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    readonly_fields = ('updated_date',)
    summernote_fields = ('content',)
    # fields = ('title', 'content','counted_view', 'status', 'updated_date', 'published_date')
    # exclude = ('content',)
    # ordering = ('counted_view', 'created_date')
    # description=('Full name of the person',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '????'
    list_display = ('name', 'post','email', 'subject','updated_date', 'created_date', 'approved')
    list_filter = ('name', 'subject', 'approved')
    search_fields = ['name', 'message', 'subject']
    readonly_fields = ('updated_date',)
    # summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
