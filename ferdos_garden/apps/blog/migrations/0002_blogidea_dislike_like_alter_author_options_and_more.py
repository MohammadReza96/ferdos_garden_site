# Generated by Django 4.1.2 on 2022-11-03 22:17

import apps.blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='full_name')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('register_date', models.DateField(default=django.utils.timezone.now, verbose_name='register_date')),
                ('blog_idea', models.TextField(verbose_name='blog_idea')),
            ],
        ),
        migrations.CreateModel(
            name='DisLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='bloggallary',
            options={'verbose_name': 'BlogGallary', 'verbose_name_plural': 'BlogGallarys'},
        ),
        migrations.AlterModelOptions(
            name='bloggroup',
            options={'verbose_name': 'BlogGroup', 'verbose_name_plural': 'BlogGroups'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='bloggallary',
            name='blog_image',
            field=models.ImageField(upload_to=apps.blog.models.upload_service_gallary_image, verbose_name='main_image'),
        ),
    ]
