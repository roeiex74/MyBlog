from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "date")
    list_filter = ("tags", "author", "date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "user_email", "date")
    list_filter = ("name", "user_email", "date")


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
