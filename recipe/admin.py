from django.contrib import admin
from .models import Recipe, Category

admin.site.register(Recipe)
admin.site.register(Category)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
