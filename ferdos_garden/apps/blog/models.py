from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils import timezone




def upload_service_main_imgae(instance,filename):
    return f'image/article_image/{instance.blog_slug}/{filename}'

def upload_service_gallary_image(instance,filename):
    return f'image/article_gallery/{instance.blog.blog_slug}/{filename}'

#----------------------------------------------------------------------------------------
class Author(models.Model):
    author_name=models.CharField(max_length=50,verbose_name='name')
    author_family=models.CharField(max_length=50,verbose_name='family')
    author_slug=models.SlugField(max_length=50,verbose_name='slug')
    author_email=models.EmailField(max_length=255,verbose_name='email')
    author_phone=models.CharField(max_length=11,verbose_name='phone',null=True,blank=True)
    auhtor_status=models.BooleanField(default=False,verbose_name='status')
    
    def __str__(self):
        return self.author_name+' '+self.author_family
    
    class Meta:
        verbose_name='Author'
        verbose_name_plural='Authors'
        db_table='table_author'
 
#----------------------------------------------------------------------------------------
class BlogGroup(models.Model):
    group_title=models.CharField(max_length=50,verbose_name='title')
    
    def __str__(self):
        return self.group_title
    
    class Meta:
        verbose_name='BlogGroup'
        verbose_name_plural='BlogGroups'
        db_table='table_blogGroup'
        
#----------------------------------------------------------------------------------------
class Blog(models.Model):
    blog_title=models.CharField(max_length=50,verbose_name='title')
    blog_main_image=models.ImageField(upload_to=upload_service_main_imgae,verbose_name='main_image')
    blog_slug=models.SlugField(max_length=50,verbose_name='slug')
    blog_short_text=models.TextField(verbose_name='short_text')
    blog_main_text=models.TextField(verbose_name='main_text')
    blog_register_date=models.DateTimeField(auto_now_add=True,verbose_name='register_date')
    blog_publish_date=models.DateTimeField(default=timezone.now,verbose_name='publish_date')
    blog_update_date=models.DateTimeField(auto_now=True,verbose_name='update_date')
    blog_status=models.BooleanField(default=False,verbose_name='status')
    blog_view_number=models.PositiveIntegerField(default=0,verbose_name='views')
    blog_author=models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name='author')
    blog_group=models.ForeignKey(BlogGroup,on_delete=models.CASCADE,verbose_name='group')
    
    
    def __str__(self):
        return self.blog_title
    
    def blog_pgf(self,fileName):
        pass
    
    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'
        db_table='table_blog'
     
#----------------------------------------------------------------------------------------    
class Tag(models.Model):
    tag_name=models.CharField(max_length=50,verbose_name='tag')
    blog=models.ManyToManyField(Blog)
    
    def __str__(self):
        return self.tag_name
    
    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'
        db_table='table_tag'
        
#----------------------------------------------------------------------------------------
class BlogGallary(models.Model):
    blog_image=models.ImageField(upload_to=upload_service_gallary_image,verbose_name='main_image')
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name='blog')
    
    def __str__(self):
        return self.blog.blog_slug
    
    class Meta:
        verbose_name='BlogGallary'
        verbose_name_plural='BlogGallarys'
        db_table='table_blogGallary'
        

#----------------------------------------------------------------------------------------
class Like(models.Model):
    pass
class DisLike(models.Model):
    pass

#----------------------------------------------------------------------------------------
class BlogIdea(models.Model):
    blog_slug=models.SlugField(max_length=100,verbose_name='blog_slug',null=True,blank=True)
    full_name=models.CharField(max_length=100,verbose_name='نام')
    email=models.EmailField(max_length=255,verbose_name='ایمیل')
    register_date=models.DateField(default=timezone.now,verbose_name='register_date')
    blog_idea=models.TextField(verbose_name='نظر')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name='BlogIdea'
        verbose_name_plural='BlogIdeas'
        db_table='table_BlogIdea'