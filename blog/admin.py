from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '????'
    list_display = ('title','author', 'counted_view', 'status', 'updated_date', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    readonly_fields = ('updated_date',)

    # fields = ('title', 'content','counted_view', 'status', 'updated_date', 'published_date')
    # exclude = ('content',)
    # ordering = ('counted_view', 'created_date')
    # description=('Full name of the person',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
