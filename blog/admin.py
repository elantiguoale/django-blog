from django.contrib import admin
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)

# Register your models here.
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    

admin.site.register(Comment)