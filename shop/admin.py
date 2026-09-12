from django.contrib import admin
from .models import Category, Comic, ComicImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ComicImageInline(admin.TabularInline):
    model = ComicImage
    extra = 1

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'price', 'condition', 'is_sold', 'available', 'created', 'updated']
    list_filter = ['available', 'is_sold', 'condition', 'created', 'updated']
    list_editable = ['price', 'is_sold', 'available', 'condition']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ComicImageInline]
