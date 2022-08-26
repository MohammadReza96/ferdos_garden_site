from django.db import models
from django.utils import timezone


class Message(models.Model):
    first_name=models.CharField(max_length=15,verbose_name='نام')
    last_name=models.CharField(max_length=20,verbose_name='نام خانوادگی')
    email=models.EmailField(verbose_name='ایمیل')
    title=models.CharField(max_length=30,verbose_name='عنوان پیام',default='')
    text=models.TextField(verbose_name='پیام')
    is_seen_by_manager=models.BooleanField(default=False,verbose_name='وضعیت پیام')
    time_added=models.DateTimeField(default=timezone.now,verbose_name='زمان ارسال')
    
    def __str__(self):
        return self.first_name + self.last_name +self.email
    
    class Meta:
        verbose_name='پیام'
        verbose_name_plural='پیام ها'
        db_table='t_message'