from django.contrib import admin
from .models import Post
from .models import Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    list_filter = ('status','created','publish','author')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    ordering = ['status','publish']
    date_hierarchy = 'publish'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created','updated','active']
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
