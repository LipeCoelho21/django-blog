from django.contrib import admin

from blog.models import Post, Author, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date')
    list_display = ('title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)