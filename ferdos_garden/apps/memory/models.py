from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#----------------------------------------------------------------------------------
class Memory(models.Model):
    memory_title=models.CharField(max_length=50,verbose_name="عنوان خاطره")
    memory_text=models.TextField(verbose_name="متن خاطره")
    memory_register_date=models.DateField(default=timezone.now,verbose_name="تاریخ ثبت خاطره")
    memory_is_active=models.BooleanField(default=False,verbose_name="وضیت خاطره")
    user_register=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="وضعیت کاربر",null=True,blank=True)
    
    def __str__(self):
        return self.memory_title
    
    class Meta:
        verbose_name="Memory"
        verbose_name_plural="Memories"
        db_table="table_memory"

#----------------------------------------------------------------------------------
def memory_image_upload(instance,filename):
    return f'image/memory/{instance.memory.memory_title}/{filename}'


class MemoryGallary(models.Model):
    memory_image=models.FileField(upload_to=memory_image_upload,verbose_name="تصویر خاطره",null=True,blank=True)
    memory=models.ForeignKey(Memory,on_delete=models.CASCADE,verbose_name="عنوان خاطره",related_name='image',null=True,blank=True)
    
    class Meta:
        verbose_name="MemoryGallary"
        verbose_name_plural="MemoryGallaries"
        db_table="table_memory_gallary"

# by adding related_name field , we create a direct conection between tables that have 1toMany or ManytoMany relation . in fact we add a virtual field to father table 

#----------------------------------------------------------------------------------
class MemoryLike(models.Model):
    user_like=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر",null=True,blank=True)
    memory=models.ForeignKey(Memory,on_delete=models.CASCADE,verbose_name="عنوان خاطره",null=True,blank=True)

    class Meta:
        verbose_name="MemoryLike"
        verbose_name_plural="MemoryLikes"
        db_table="table_memoryLike"