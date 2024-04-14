from django.contrib import admin

from RentAll.articles.models import ArticlesModel


@admin.register(ArticlesModel)
class ArticleAdminForm(admin.ModelAdmin):
    list_display = ('article_type', 'author', 'title', 'published')
    ordering = ('published',)
    list_filter = ['article_type', 'author', 'title', ]
    search_fields = ('article_type', 'author', 'title',)
    fieldsets = (
        ('Main Information', {
            'fields': ('article_type', 'author'),
        }),
        ('Titles', {
            'fields': ('title', 'sub_title'),
        }),
        ('Rest of article', {
            'fields': ('article_image', 'description',)
        })
    )
