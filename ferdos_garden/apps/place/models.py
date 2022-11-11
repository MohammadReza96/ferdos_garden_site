from tabnanny import verbose
from django.db import models
from django.utils import timezone




def upload_service_main_imgae(instance,filename):
    return f'image/places/main_image/{instance.place_slug}/{filename}'

# def upload_service_gallary_imgae(instance,filename):
#     return f'images/services/gallary/{instance.service.service_slug}/{filename}'



#####################################################################################
class Place(models.Model):
    place_name=models.CharField(max_length=50,verbose_name='name')
    place_slug=models.SlugField(max_length=10,verbose_name='slug')
    place_information=models.TextField(verbose_name='information')
    place_image_name=models.ImageField(upload_to=upload_service_main_imgae,verbose_name='place_image_name',null=True,blank=True)
    visiting_day=models.CharField(max_length=50,verbose_name='visiting_day',null=True,blank=True)
    visiting_hour=models.CharField(max_length=50,verbose_name='visiting_hour',null=True,blank=True)
    register_date=models.DateTimeField(default=timezone.now,verbose_name='register_date')

    def __str__(self):
        return self.place_name
    
    class Meta:
        verbose_name='place'
        verbose_name_plural='places'
        db_table='table_place'
        
#####################################################################################
class Rule(models.Model):
    title=models.TextField(verbose_name='title')
    place=models.ManyToManyField(Place)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='rule'
        verbose_name_plural='rules'
        db_table='table_rule'
        
#####################################################################################
class VisitorType(models.Model):
    visitor_type=models.CharField(max_length=50,verbose_name='visitor_type')
    
    def __str__(self):
        return self.visitor_type
    
    class Meta:
        verbose_name='visitor_type'
        verbose_name_plural='visitor_types'
        db_table='table_visitor_type'
        
#####################################################################################
class Ticket(models.Model):
    visitor_type=models.ForeignKey(VisitorType,on_delete=models.CASCADE,verbose_name='visitor_type')
    place=models.ForeignKey(Place,on_delete=models.CASCADE,verbose_name='place')
    price=models.FloatField(default=0,verbose_name='price')
    
    def __str__(self):
        return f'{self.place}+{self.visitor_type}+{self.price}'
    
    class Meta:
        verbose_name='Ticket_price'
        verbose_name_plural='Ticket_prices'
        db_table='table_Ticket_price'
        ordering = ['place']
