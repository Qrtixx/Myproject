from django.contrib import admin
from .models import Article, Category, Comment, Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish_date')
    list_filter = ('category', 'publish_date')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
