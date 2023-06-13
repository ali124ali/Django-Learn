from django.contrib import admin
from website.models import Contact, Newsletter

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_date', 'updated_date')
    search_fields = ('message',)
    date_hierarchy = 'created_date'
    list_filter = ('email',)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Contact, WebsiteAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
