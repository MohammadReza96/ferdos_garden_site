# Generated by Django 4.1.2 on 2022-11-10 21:51

import apps.memory.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorygallary',
            name='memory_image',
            field=models.FileField(blank=True, null=True, upload_to=apps.memory.models.memory_image_upload, verbose_name='تصویر خاطره'),
        ),
        migrations.AlterField(
            model_name='memorylike',
            name='memory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='memory.memory', verbose_name='عنوان خاطره'),
        ),
        migrations.AlterField(
            model_name='memorylike',
            name='user_like',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]