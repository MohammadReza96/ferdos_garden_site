# Generated by Django 4.1.2 on 2022-10-30 20:45

import apps.blog.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='name')),
                ('author_family', models.CharField(max_length=50, verbose_name='family')),
                ('author_slug', models.SlugField(verbose_name='slug')),
                ('author_email', models.EmailField(max_length=255, verbose_name='email')),
                ('author_phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='phone')),
                ('auhtor_status', models.BooleanField(default=False, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Authors',
                'db_table': 'table_author',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50, verbose_name='title')),
                ('blog_main_image', models.ImageField(upload_to=apps.blog.models.upload_service_main_imgae, verbose_name='main_image')),
                ('blog_slug', models.SlugField(verbose_name='slug')),
                ('blog_short_text', models.TextField(verbose_name='short_text')),
                ('blog_main_text', models.TextField(verbose_name='main_text')),
                ('blog_register_date', models.DateTimeField(auto_now_add=True, verbose_name='register_date')),
                ('blog_publish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publish_date')),
                ('blog_update_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('blog_status', models.BooleanField(default=False, verbose_name='status')),
                ('blog_view_number', models.PositiveIntegerField(default=0, verbose_name='views')),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author', verbose_name='author')),
            ],
            options={
                'verbose_name': 'Blogs',
                'db_table': 'table_blog',
            },
        ),
        migrations.CreateModel(
            name='BlogGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_title', models.CharField(max_length=50, verbose_name='title')),
            ],
            options={
                'verbose_name': 'BlogGroups',
                'db_table': 'table_blogGroup',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, verbose_name='tag')),
                ('blog', models.ManyToManyField(to='blog.blog')),
            ],
            options={
                'verbose_name': 'Tags',
                'db_table': 'table_tag',
            },
        ),
        migrations.CreateModel(
            name='BlogGallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image', models.ImageField(upload_to=apps.blog.models.upload_service_main_imgae, verbose_name='main_image')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='blog')),
            ],
            options={
                'verbose_name': 'BlogGallarys',
                'db_table': 'table_blogGallary',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.bloggroup', verbose_name='group'),
        ),
    ]
