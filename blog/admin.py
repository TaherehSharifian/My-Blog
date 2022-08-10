from django.contrib import admin

from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'author')
    prepopulated_fields = {'slug': ('title', )}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment, CommentAdmin)