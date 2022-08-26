from django.db import models
from django.utils import timezone





class Author(models.Model):
    name=models.CharField(max_length=200,verbose_name='نام')
    family=models.CharField(max_length=200,verbose_name='نام خانوادگی')
    author_image=models.ImageField(upload_to='image/authors',verbose_name='تصویر نویسنده')
    author_slug=models.SlugField(max_length=200,verbose_name='کلید نویسنده')
    author_email=models.EmailField(max_length=200,null=True,blank=True,verbose_name='ایمیل نویسنده')
    author_mobile=models.CharField(max_length=11,null=True,blank=True,verbose_name='تلفن همراه نویسنده')
    is_active=models.BooleanField(default=False,verbose_name='وضعیت نویسنده')
    
    def __str__(self):
        return self.name + self.family
    class Meta:
        verbose_name='نویسنده'
        verbose_name_plural='نویسندگان'
        db_table='t_author'




class Article_Group(models.Model):
    group_title=models.CharField(max_length=20,verbose_name='گروه مقاله')
    
    def __str__(self):
        return self.group_title
    class Meta:
        verbose_name='گروه مقاله'
        verbose_name_plural='گروه مقالات'
        db_table='t_group_title'






class Key_Word(models.Model):
    key_word=models.CharField(max_length=20,verbose_name='کلمه کلیدی')
    
    def __str__(self):
        return self.key_word
    class Meta:
        verbose_name='کلمه کلیدی'
        verbose_name_plural='کلمات کلیدی'
        db_table='t_key_word'






class Article(models.Model):
    group=models.ForeignKey(Article_Group,on_delete=models.CASCADE,verbose_name='گروه مقاله')
    title=models.CharField(max_length=200,verbose_name='عنوان مقاله')
    article_slug=models.SlugField(max_length=200,verbose_name='کلید مقاله')
    article_main_image=models.ImageField(upload_to='image/blog_image',verbose_name='عکس اصلی مقاله')
    article_author=models.ManyToManyField(Author,verbose_name='نویسنده مقاله')
    article_summery=models.TextField(verbose_name='خلاصه مقاله')
    article_text=models.TextField(verbose_name='متن مقاله')
    article_key_word=models.ManyToManyField(Key_Word,verbose_name='کلمه کلیدی')
    article_register_date=models.DateField(auto_now_add=True,verbose_name='تاریخ درج')
    article_publish_date=models.DateField(default=timezone.now,verbose_name='تاریخ انتشار')
    article_update_date=models.DateField(auto_now=True,verbose_name='تاریخ اخرین آپدیت')
    is_active=models.BooleanField(default=False,verbose_name='وضعیت مقاله')
    article_pdf_file=models.CharField(max_length=200,verbose_name='فایل  پی دی اف مقاله')
    article_number_seen=models.PositiveSmallIntegerField(default=0,verbose_name='تعداد بازدید کنندگان')
    
    def __str__(self):
        return self.title 
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'
        db_table='t_article'




class Article_Gallary(models.Model):
    article_image=models.ImageField(upload_to='image/blog_image',verbose_name='تصویر مقاله')
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='نام مقاله')
    def __str__(self):
        return str(self.article_image)
    class Meta:
        verbose_name='تصویر'
        verbose_name_plural='تصاویر'
        db_table='t_article_image'