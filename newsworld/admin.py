from django.contrib import admin

from newsworld.models import NewsCategory, News, MyUserModel


# Register your models here.

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_filter = ['created_at']
    list_display = ['category_name', 'created_at']

admin.site.register(News)

@admin.register(MyUserModel)
class MyUserModelAdmin(admin.ModelAdmin):
    search_fields = ['username', 'id']
    list_display = ['username', 'id', 'phone_number', 'email']
    ordering = ['-id']