from django.contrib import admin

from newsworld.models import NewsCategory, News


# Register your models here.

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_filter = ['created_at']
    list_display = ['category_name', 'created_at']

admin.site.register(News)