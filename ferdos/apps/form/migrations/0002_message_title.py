# Generated by Django 4.1 on 2022-08-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default='', max_length=30, verbose_name='عنوان پیام'),
        ),
    ]