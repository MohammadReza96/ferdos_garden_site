# Generated by Django 4.1.2 on 2022-11-09 20:10

import apps.memory.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory_title', models.CharField(max_length=50, verbose_name='عنوان خاطره')),
                ('memory_text', models.TextField(verbose_name='متن خاطره')),
                ('memory_register_date', models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ ثبت خاطره')),
                ('memory_is_active', models.BooleanField(default=False, verbose_name='وضیت خاطره')),
                ('user_register', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='وضعیت کاربر')),
            ],
            options={
                'verbose_name': 'Memory',
                'verbose_name_plural': 'Memories',
                'db_table': 'table_memory',
            },
        ),
        migrations.CreateModel(
            name='MemoryLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='memory.memory', verbose_name='عنوان خاطره')),
                ('user_like', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'MemoryLike',
                'verbose_name_plural': 'MemoryLikes',
                'db_table': 'table_memoryLike',
            },
        ),
        migrations.CreateModel(
            name='MemoryGallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory_image', models.FileField(upload_to=apps.memory.models.memory_image_upload, verbose_name='تصویر خاطره')),
                ('memory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='memory.memory', verbose_name='عنوان خاطره')),
            ],
            options={
                'verbose_name': 'MemoryGallary',
                'verbose_name_plural': 'MemoryGallaries',
                'db_table': 'table_memory_gallary',
            },
        ),
    ]
