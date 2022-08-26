from django.contrib import admin
from apps.blog.models import Author,Article_Group,Article,Key_Word,Article_Gallary

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','family','author_image','author_slug','author_email','author_mobile','is_active')
    
    
    
@admin.register(Article_Group)
class Article_GroupAdmin(admin.ModelAdmin):
    list_display=('group_title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('group','title','article_slug','article_main_image','article_summery','article_text','article_register_date','article_publish_date','article_update_date','is_active','article_pdf_file','article_number_seen')

Article_Gallary
@admin.register(Key_Word)
class Key_WordAdmin(admin.ModelAdmin):
    list_display=('key_word',)

@admin.register(Article_Gallary)
class Article_GallaryAdmin(admin.ModelAdmin):
    list_display=('article_image','article')