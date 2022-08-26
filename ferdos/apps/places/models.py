from django.db import models
from django.utils import timezone

#------------------------------------------------------------- class place
class Place(models.Model):
    place_name=models.CharField(max_length=100,verbose_name='نام مکان')
    information=models.TextField(default='توضیحات',verbose_name='توضیحات')
    place_image=models.ImageField(verbose_name='عکس',upload_to='image/places/')
    visiting_day=models.CharField(verbose_name='روز های بازدید',max_length=100)
    visiting_hour=models.CharField(max_length=100,verbose_name='ساعات بازدید')
    rules=models.TextField(verbose_name='قوانین و مقررات',default='رعایت حجاب اسلامی')
    register_date=models.DateTimeField(verbose_name='تاریخ ثبت',default=timezone.now)
    
    def __str__(self):
        return self.place_name
    class Meta:
        verbose_name='مکان'
        verbose_name_plural='مکان ها'
        db_table='t_places'
    
#------------------------------------------------------------- class visitor type
class Visitor_Type(models.Model):
    type_name=models.CharField(max_length=100,verbose_name='نوع بازدید کننده')
    def __str__(self):
        return self.type_name
    class Meta:
        verbose_name='نوع بازدید کننده'
        verbose_name_plural='نوع بازدید کننده ها'
        db_table='t_visitor_type'
        
#------------------------------------------------------------- class ticket price
class Ticket_price(models.Model):
    place=models.ForeignKey(Place,on_delete=models.CASCADE,verbose_name="مکان")
    visitor_type=models.ForeignKey(Visitor_Type,on_delete=models.CASCADE,verbose_name='نوع بازدید کننده')
    price=models.IntegerField(default=0,verbose_name='بهای بلیط')
    
    def __str__(self):
        return f'{self.place} {self.visitor_type} {self.price}'
    class Meta:
        verbose_name='قیمت '
        verbose_name_plural='قیمت ها'
        db_table='t_ticket_price'
    
    