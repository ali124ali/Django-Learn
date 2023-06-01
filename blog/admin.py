from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '????'
    # fields = ('title', 'counted_view', 'status')
    # exclude = ('content',)
    list_display = ('title', 'counted_view', 'status', 'updated_date', 'created_date', 'published_date')
    # ordering = ('counted_view', 'created_date')
    # description=('Full name of the person',)
    list_filter = ('status',)
    search_fields = ['title', 'content']
    readonly_fields = ('updated_date',)



admin.site.register(Post, PostAdmin)
