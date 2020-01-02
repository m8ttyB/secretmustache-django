from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'last_modified',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)