from django.contrib import admin
from .models import Post, Category, Tag

class CateAdmin(admin.ModelAdmin):
    list_display = ['name']
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CateAdmin)
admin.site.register(Tag,TagAdmin)