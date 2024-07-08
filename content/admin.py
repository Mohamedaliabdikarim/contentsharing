from django.contrib import admin
from .models import Content, Category

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

#     def has_add_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False

admin.site.register(Category)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'updated_at')
    list_filter = ('owner', 'created_at', 'categories')
    search_fields = ('title', 'content', 'owner__username', 'categories__name')
    filter_horizontal = ('categories',)
