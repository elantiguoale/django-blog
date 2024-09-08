from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Comment

@admin.register(Post)

# Register your models here.
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    

admin.site.register(Comment)