from django.contrib import admin
from .models import Author,BlogGroup,Blog,Tag,BlogGallary,BlogIdea


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('author_name','author_family','auhtor_status','author_email')
    prepopulated_fields={'author_slug':('author_name','author_family')}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('blog_title','blog_author','blog_group','blog_update_date','blog_register_date','blog_view_number','blog_status')
    prepopulated_fields={'blog_slug':('blog_title',)}

@admin.register(BlogGroup)
class BlogGroupAdmin(admin.ModelAdmin):
    list_display=('group_title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('tag_name',)
    
@admin.register(BlogGallary)
class BlogGallaryAdmin(admin.ModelAdmin):
    list_display=('blog_image','blog')
    
@admin.register(BlogIdea)
class BlogIdeaAdmin(admin.ModelAdmin):
    list_display=('full_name','register_date')
