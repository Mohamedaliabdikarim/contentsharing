from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at', 'updated_at', 'image_filter')

    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'Category'
