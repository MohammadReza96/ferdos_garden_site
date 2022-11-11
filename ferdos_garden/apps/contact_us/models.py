from django.db import models
from django.utils import timezone


class ContactModel(models.Model):
    name=models.CharField(max_length=50,verbose_name='name')
    family=models.CharField(max_length=50,verbose_name='family',null=True,blank=True)
    title=models.CharField(max_length=50,verbose_name='title')
    email=models.EmailField(verbose_name='email')
    register_time=models.DateTimeField(default=timezone.now,verbose_name='register_time')
    message=models.TextField(verbose_name='message')


    def __str__(self):
        return self.name+' '+self.family
    class Meta:
        verbose_name='form'
        verbose_name_plural='forms'
        db_table='table_contactform'
